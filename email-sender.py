import smtplib
from getpass import getpass
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)


def login():
    email = input('Email (followed by enter):\n')
    password = getpass('Password (followed by enter):\n')
    smtpObj.login(email, password)
    return email


def sendMsg(email):
    target = input("Enter the recipient's address:\n")
    subject = input("Enter the subject:\n")
    body = input("Enter the body of the msg:\n")
    payload = "From:" + email + "\r\n" + "To:" + target + \
        "\r\n" + "Subject:" + subject + "\r\n" + body
    smtpObj.sendmail(email, target, payload)


try:
    email = login()
    print('Success!')
    sendMsg(email)
    print('Successfully sent!')

except:
    print("Something went wrong. Please check your email and password.\nIf this message still shows up, please allow third party programs to access your google account by this link: https://myaccount.google.com/lesssecureapps")
