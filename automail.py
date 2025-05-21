
import os
import random
import smtplib


def automatic_email():
    user = input("Enter Your Name >>: ")
    email = input("Enter Your Email >>: ")
    message = (f"Dear {user}, Welcome to Thecleverprogrammer")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("modihimanshu66@gmail.com", "ejxdddusaixssgqx")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!")
    
automatic_email()