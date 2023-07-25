# importing Library
import random
import smtplib
from email.message import EmailMessage

# Function for otp
def generate_otp():
    return random.randint(100000,999999)

# Function for email sending
def sending_email(user_email,otp):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'agaur3512@gmail.com'
    smtp_password = 'izuorwkaemyqdser'

    # sending message
    msg = EmailMessage()
    msg.set_content(f"your otp is : {otp}")
    msg["subject"] = "otp verification"
    msg["From"] = smtp_username
    msg["To"] = user_email

    # set up server
    with smtplib.SMTP(smtp_server,smtp_port)as server:
        server.starttls()
        server.login(smtp_username,smtp_password)
        server.send_message(msg)

def main():
    otp = generate_otp()
    user_email = input("Enter your email : ")
    sending_email(user_email,otp)
    v_otp = input("Enter your otp : ")
    if v_otp == str(otp):
        print("otp verified successfully")
    else:
        print("otp verification failed!")

if __name__ == "__main__":
    main()
