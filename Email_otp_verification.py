import math as m
import random as r
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def otp_on_email(email_id):
    fromAdd = "-----Enter your Email-----"
    senders_pass = "---Enter your Password--"
    toAdd = email_id

    msg=MIMEMultipart()
    msg['From']=fromAdd
    msg['To']=toAdd
    msg['Subject']="Urban AId  -OTP"

    # # genrate randome numbers
    # OTP =r.randrange(100001,999999)

    # if you want use Strings and numbers
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = "" 
    varlen= len(string) 
    for i in range(8) : 
        OTP += string[m.floor(r.random() * varlen)] 

    body = """

            Your OTP Is [ {} ] and you can use it for change Your Account password .  
            _______________________________________________________________________
            @Team Vihan Mehta
            
            """.format(OTP)
    
    msg.attach(MIMEText(body, 'plain'))
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(fromAdd,senders_pass)
    text=msg.as_string()
    s.sendmail(fromAdd,toAdd,text)
    s.quit()
    c_txt="OTP send on your email ({}*******{})".format(toAdd[0:2],toAdd[6:])
    print(c_txt)
    return OTP

entered_email_id=input("Enter your valid Email ID : ")
generated_otp=otp_on_email(entered_email_id)
user_enterd_otp=input("Enter OTP :")
if generated_otp==user_enterd_otp:
    print("OTP matched ")
else:
    print("You enterd wrong OTP")
