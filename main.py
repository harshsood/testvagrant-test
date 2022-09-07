from tkinter import *
import time
from tkinter import messagebox
import os
import smtplib
from email.message import EmailMessage
from random import randint

color='#87918c'
color1='#757d79'
color3='#bf5454'      #exit button
color4='#87918c'
color5='#87918c'
color6='#87918c'
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')  # your email address
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')  # password
x = randint(99, 200)
path = 'C:\\Users\\Harsh Sood\\PycharmProjects\\billing_management.py\\bills'  #path to the folder
root = Tk()
root.geometry("1150x750+0+0")
root.title("Restaurant Billing System")
Tops = Frame(root, width=1350, height=50, bd=8, bg=color, relief="raise")
Tops.pack(side=TOP)
Bottoms = Frame(root, width=1350, height=50, bd=8, bg=color, relief="raise")
Bottoms.pack(side=BOTTOM)
f1 = Frame(root, width=900, height=650, bd=8, bg=color, relief="raise")
f1.pack(side=LEFT)
f1a = Frame(f1, width=900, height=330, bd=8, bg=color, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=8, bg=color, relief="raise")
f2a.pack(side=BOTTOM)
f1aa = Frame(f1a, width=400, height=430, bd=8, bg=color4, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=8, bg=color5, relief="raise")
f1ab.pack(side=RIGHT)
f2aa = Frame(f2a, width=450, height=330, bd=8, bg=color6, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=8, bg=color4, relief="raise")
f2ab.pack(side=LEFT)
lblInfo = Label(Tops, font=('arial', 25, 'bold'), text="Restaurant Billing System", bg=color,bd=15,padx=12, anchor='w')
lblInfo.grid(row=0, column=0)

# ==============================Variables=====================
PaymentRef = StringVar()
emailID = StringVar()
wallet = StringVar()
honey = StringVar()
cigeratte = StringVar()
umbrella = StringVar()
costwallet = StringVar()
costumbrella = StringVar()
costhoney = StringVar()
costcigeratte = StringVar()
dateRef = StringVar()
subTotal = StringVar()
gst = StringVar()
totalPrice = StringVar()
text_Input = StringVar()
dateRef.set(time.strftime("%d/%m/%y"))
operator = ""
gst.set(0)

subTotal.set(0)
totalPrice.set(0)
costwallet.set(110)
costhoney.set(180)
costcigeratte.set(200)
costumbrella.set(900)
emailID.set("Enter_EmailID")

# =============================Functions==================
def tPrice():
    cBprice = int(costwallet.get())
    bBprice = int(costhoney.get())
    fFprice = int(costcigeratte.get())
    sDprice = int(costumbrella.get())
    tempgst = int(gst.get())
    subPrice = (bBprice * bBno + fFprice * fFno + sDprice * sDno)
    totalCost = str('%d' % subPrice)
    totalCostwithVat = str('%d' % (subPrice + (subPrice * tempgst) / 100))
    subTotal.set(totalCost)
    totalPrice.set(totalCostwithVat)

def iExit():
    qexit = messagebox.askyesno("Billing System", "Do you want to exit?")
    if qexit > 0:
        root.destroy()
        return

def reset():
    global x
    x = x + 1
    PaymentRef.set("")
    wallet.set(0)
    umbrella.set(0)
    cigeratte.set(0)
    honey.set(0)
    subTotal.set(0)
    totalPrice.set(0)
    emailID.set("Enter EmailID")

def refNo():
    global x
    y = str(x)
    randomRef = str(y)
    PaymentRef.set("BILL" + randomRef)

def create_bill():
    global x
    refno = str(x)
    pakodi = refno + ".txt"
    global path
    with open(os.path.join(path, pakodi), "w") as file1:
        toFile = output()
        file1.write(toFile)
    qmsg = messagebox.showinfo("Information", "Bill Generated")

def send_bill():
    #
    msg = EmailMessage()
    msg['Subject'] = 'Your bill '
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = emailID.get()+'@gmail.com' # receiver email
    print(emailID.get())
    global x
    fileref = str(x) + '.txt'
    msg.set_content('This is your Total bill \n your Reference.No is: Bill' + str(x))
    with open(os.path.join(path, fileref), "rb") as f:
        file_data = f.read()
        file_name = "RestaurentBill"
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    qsend = messagebox.askyesno("Billing System", "Do you want to send the bill?")
    if qsend > 0:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        qsmsg = messagebox.showinfo("Information", "Bill send successfully")
    else:
        qnmsg = messagebox.showinfo("Information", "Bill  will not send")

def output():
    global x
    refno = str(x)
    list0 = "\t\t\t\t\tReference.no :" + refno
    list02='\t\t\t\tEmailID :'+emailID.get()+'@gmail.com'
    list1 = "\n\n" + "Item\t\t\tQuantity\t\tCost\n"
    list7 = "____\t\t\t_______\t\t        ____\n\n"
    list2 = "wallet\t\t\t" + wallet.get() + "\t\t\t" + str(int(wallet.get()) * int(costwallet.get())) + "\n"
    list3 = "umbrella\t\t\t" + umbrella.get() + "\t\t\t" + str(int(umbrella.get()) * int(costumbrella.get())) + "\n"
    list4 = "cigeratte\t" + cigeratte.get() + "\t\t\t" + str(
        int(costcigeratte.get()) * int(cigeratte.get())) + "\n"
    list5 = "honey\t\t\t" + honey.get() + "\t\t\t" + str(int(honey.get()) * int(costhoney.get())) + "\n"
    list6 = "\t\t\t   " + "total     = Rs " + subTotal.get() + "/-" + "\n"
    list8 = "\t\t\t   " + "gst      = Rs " + str(int(totalPrice.get()) - int(subTotal.get())) + "/-" + "\n"
    list9 = "\t\t\t   " + "GrandTotal= Rs " + totalPrice.get()[:] + "/-" + "\n"
    String = list0 +list02+ list1 + list7 + list2 + list3 + list4 + list5 + list6 + list8 + list9
    return String

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

# ==================================Order Info===========================
lblRef = Label(f1aa, font=('arial', 16, 'bold'), fg="red", text="Reference No", bd=16, bg=color4, justify='left')
lblRef.grid(row=0, column=0)
txtRef = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=PaymentRef, bd=10, insertwidth=2, justify='left')
txtRef.grid(row=0, column=1)
# --------------
lblCb = Label(f1aa, font=('arial', 16, 'bold'), text="Leather Wallet", bd=16, bg=color4, justify='left')
lblCb.grid(row=1, column=0)
txtCb = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=wallet, bd=10, insertwidth=2, justify='left')
txtCb.grid(row=1, column=1)
# --------------
lblBb = Label(f1aa, font=('arial', 16, 'bold'), text="Umbrella", bd=16, bg=color4, justify='left')
lblBb.grid(row=2, column=0)
txtBb = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=umbrella, bd=10, insertwidth=2, justify='left')
txtBb.grid(row=2, column=1)
# --------------
lblFf = Label(f1aa, font=('arial', 16, 'bold'), text="Cigeratte", bd=16, bg=color4, justify='left')
lblFf.grid(row=3, column=0)
txtFf = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=cigeratte, bd=10, insertwidth=2, justify='left')
txtFf.grid(row=3, column=1)
# --------------
lblSd = Label(f1aa, font=('arial', 16, 'bold'), text="Honey", bd=16, bg=color4, justify='left')
lblSd.grid(row=4, column=0)
txtSd = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=honey, bd=10, insertwidth=2, justify='left')
txtSd.grid(row=4, column=1)
# ===================================Payment Info==========================

# ==========================Total Payment Info======
lblPrice = Label(f2aa, font=('arial', 16, 'bold'), text="Price", bd=16, bg=color6, justify='left')
lblPrice.grid(row=0, column=0)
txtPrice = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=subTotal, bd=10, insertwidth=2, justify='left')
txtPrice.grid(row=0, column=1)
# --------------
lblVat = Label(f2aa, font=('arial', 16, 'bold'), text="GST", bd=16, bg=color6, justify='left')
lblVat.grid(row=1, column=0)
txtVat = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=gst, bd=10, insertwidth=2, justify='left')
txtVat.grid(row=1, column=1)
# --------------
lblTp = Label(f2aa, font=('arial', 16, 'bold'), text="Total Price", bd=16, bg=color6, justify='left')
lblTp.grid(row=2, column=0)
txtTp = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=totalPrice, bd=10, insertwidth=2, justify='left')
txtTp.grid(row=2, column=1)
# ----------------
lblTp = Label(f2aa, font=('arial', 16, 'bold'), text="EMAIL-ID", bd=16, bg=color6, justify='left')
lblTp.grid(row=3, column=0)
txtTp = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=emailID, bd=10, insertwidth=2, justify='left')
txtTp.grid(row=3, column=1)
# ==============Buttons==========
btnTotal = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Total Price", bg=color, command=tPrice).grid(row=1, column=0)
btnRefer = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Sales Reference", bg=color, command=refNo).grid(row=0, column=0)
btnCrtb = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=10,
                 text="Generate bill", bg=color1, command=create_bill).grid(row=0, column=2)
btnReset = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                  text="Reset", bg=color, command=reset).grid(row=0, column=1)
btnExit = Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial', 16, 'bold'), width=15,
                 text="Exit", bg=color3, command=iExit).grid(row=1, column=1)

root.mainloop()
