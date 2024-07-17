# Anthony Tommaso
# December 27th, 2023
# Personal Project #1: Creatine Reminder
# The purpose of this program is to operate around the clock, and providing a
# daily reminder at a specified time of day, every day, until the user seizes the programs
# lifespan. Using both computer notification & Google Email services, a reminder will be sent
#to the user simultaneously reminding them to take their supplement, Creatine.

import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from plyer import notification

sender_email = 'Sonic99090@gmail.com' #MY email
sender_password = 'joeh oeae pfwq lmis' #app-generated password; not real
recipient_email = 'Sonic99090@gmail.com' #sending to myself
smtp_server = 'smtp.gmail.com' #connecting SMTP to gmail server
smtp_port = 587 #designated email port, standard

def send_notif(): #creating function for notification for my PC
    title = "Creatine Reminder" #notif header
    message = "Take your 1 ~ 2 tbsp of creatine!!!" #notif body
    notification.notify( 
        title = title,
        message = message,
        timeout = 10
        )

def send_email(): #creating function for actual email
    subject = "Creatine Reminder" #email subject
    body = "DON'T FORGET TO TAKE UR TBSP OF CREATINE TODAY!!!" #email body

    msg = MIMEMultipart() #container for email using imported library
    msg['From'] = sender_email #who is sending the email
    msg['To'] = recipient_email #sending to whom
    msg['Subject'] = subject 

    msg.attach(MIMEText(body, 'plain')) #body is actual text, plain is plain text
    #instead of HTML

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls() #at specified time, server will start up and send
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

def creatine_reminder(): #function for specific time
    while True: #continuous loop until 
        current_time = time.strftime("%H:%M") #formatting time for hours and minutes
        if current_time == "07:02":
            send_notif()
            send_email()
            print("Notifcation and email sent.") #notification sent to computer
            break #exit after sending reminder
        time.sleep(60) 

if __name__ == "__main__":
    creatine_reminder()
