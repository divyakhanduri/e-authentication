import os
import math
import random
import smtplib
import pyqrcode         #how to generate otp
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("khanduridivya1@gmail.com", "veupowkbwihqbhlb")

emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified\n")
    ch=int(input("Enter 1 to open your G-mail\nEnter 2 to open your ERP\nEnter your linkedin page::-\n"))
    if ch ==1:
        s  = "https://mail.google.com/mail/u/0/#inbox"
        url = pyqrcode.create(s)
        url.svg("qr.svg", scale=10)
        print("now  scan qr code::-\n")
    elif ch==2:
        s = "http://student.geu.ac.in/Account/Cyborg_StudentMenu#"
        url = pyqrcode.create(s)
        url.svg("qr.svg", scale=10)
        print("now  scan qr code::-\n")
    elif ch==3:
        s = "https://www.linkedin.com/feed/"
        url = pyqrcode.create(s)
        url.svg("qr.svg", scale=10)
        print("now  scan qr code::-\n")
    else:
        print("Thankyou::-\n")
else:
    print("Please Check your OTP again")