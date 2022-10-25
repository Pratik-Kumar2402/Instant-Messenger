import time
from getpass import getpass
import imaplib
import mysql.connector
import smtplib
from email.message import EmailMessage
import webbrowser
from datetime import datetime

print(end="NOTE: Importing Modules")
for x in range(3):
    print(end=".")
    time.sleep(0.7)

print("""\n\nNOTE: THESE PROGRAM MAY NOT WORK UNLESS YOU HAVE ACTIVATED
GOOGLE FEATURE NAMED: LESS SECURE APP, FOR YOUR ACCOUNT...\n\n""")

info=input("Confirm where you have enabled less secure app for your account(Y/N) : ").upper()
if info == 'Y' or info == 'YES':
    print("")
elif info == 'N' or info == 'NO' :
    print("\nFirst Enable the Option then Come Back")
    time.sleep(1.5)
    webbrowser.open('https://myaccount.google.com/lesssecureapps', new=7)
    
    print(end='Exiting')
    for x in range(3):
        print(end='.')
        time.sleep(0.7)
    exit()
else :
    print("\n\tWrong Entry...")

while 1:
    ch=int(input("""\n1. Pin.
2. Password.
\nChoice your method for password input : """))
    if ch == 1:
        pw=int(getpass("\nPlease Enter the Pin : "))
        if pw == 7098:
            print("\n\t-| Welcome Sir/Madam |-")
            break
        elif pw != 7098:
            print("\nWarning, wrong password besure what you type in.")

            pw=int(getpass("\nPlease Enter the Pin : "))
            if pw == 7098:
                print("\n\t-| Welcome Sir/Madam |-")
                break
            elif pw != 7098:
                print("""\nWarning, wrong password besure what you type in.
NOTE: Last chance""")
                pw=int(getpass("\nPlease Enter the Pin : "))
                if pw == 7098:
                    print("\n\t-| Welcome Sir/Madam |-")
                    break
                elif pw != 7098:
                    print(end="Exit")
                    for x in range(3):
                        print(end=".")
                        time.sleep(0.7)
                    exit()
        
    elif ch == 2:
        pw=str(getpass("\nPlease Enter the Password : "))
        if pw == 'pratik_kumar':
            print("\n\t-| Welcome Sir/Madam |-")
            break
        elif pw != 'pratik_kumar':
            print("\nWarning, wrong password besure what you type in.")

            pw=str(getpass("\nPlease Enter the Password : "))
            if pw == 'pratik_kumar':
                print("\n\t-| Welcome Sir/Madam |-")
                break
            elif pw != 'pratik_kumar':
                print("""\nWarning, wrong password besure what you type in.
NOTE: Last chance""")
                pw=str(getpass("\nPlease Enter the Password : "))
                if pw == 'pratik_kumar':
                    print("\n\t-| Welcome Sir/Madam |-")
                    break
                elif pw != 'pratik_kumar':
                    print(end="Exit")
                    for x in range(3):
                        print(end=".")
                        time.sleep(0.7)
                    exit()
    else :
        print("\n\tInvalid Entry...")

time.sleep(1)
print(end="\nStarting your program")
for x in range(3):
    print(end='.')
    time.sleep(0.7)
    
print("\n\n---------| WELCOME TO INSTANT MESSENGER |---------\n")
time.sleep(0.7)
    
con = str(input("Do you want to store the sent emails(Y/N) : ")).upper()
if con == 'Y' or con == 'YES':
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="7098")
        mycursor=mydb.cursor()
    
        time.sleep(1.5)
        print("\n\tCreating Database and Table for Storing Sended Emails offline\n")

        try:
            mycursor.execute("CREATE DATABASE 12sci")
            mydb.commit()
            time.sleep(1)
            print('\nDatabase Created...')
        except:
            time.sleep(0.7)
            print('\nDatabase Alredy Exist...')

        print("\n-------------------*-------------------\n")

        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="7098",
            database="12sci")
        mycursor=mydb.cursor()

        try:
            mycursor.execute("""CREATE TABLE messenger(email_address varchar(40),
                            email_receiver varchar(40),
                            Subject varchar(50),
                            content varchar(2500),
                            Date_Time varchar(30))""")
            mydb.commit()
            time.sleep(1.5)
            print("\nTable Titled Messenger Created for Storing Data...")
            time.sleep(0.7)
            
        except:
            time.sleep(0.7)
            print('\nTable Messenger already exist...\n')
            time.sleep(0.7)
        
        print("\n-------------------*-------------------\n")

elif con == 'N' or con ==  'NO':
    con_2 = str(input("\nOK!, But you won't be able to view the sent emails are you sure(Y/N) : ")).upper()
    if con_2 == 'Y' or con_2 ==  'YES':
        print("OK...")
        
    elif con_2 == 'N' or con_2 ==  'NO':
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="7098")
        mycursor=mydb.cursor()
    
        time.sleep(1.5)
        print("\n\tCreating Database and Table for Storing Sended Emails offline\n")

        try:
            mycursor.execute("CREATE DATABASE 12sci")
            mydb.commit()
            time.sleep(1)
            print('\nDatabase Created...')
        except:
            time.sleep(0.7)
            print('\nDatabase Alredy Exist...')

        print("\n-------------------*-------------------\n")

        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="7098",
            database="12sci")
        mycursor=mydb.cursor()

        try:
            mycursor.execute("""CREATE TABLE messenger(email_address varchar(40),
                            email_receiver varchar(40),
                            Subject varchar(50),
                            content varchar(2500),
                            Date_Time varchar(30))""")
            mydb.commit()
            time.sleep(1.5)
            print("\nTable Titled Messenger Created for Storing Data...")
            time.sleep(0.7)
            
        except:
            time.sleep(0.7)
            print('\nTable Messenger already exist...\n')
            time.sleep(0.7)
        
    print("\n-------------------*-------------------\n")

else :
    print("\nWrong Entry...")
        
while 2:
    print("--------| LOGIN |--------")
    try:
        email_address=str(input("\nEnter Senders Email Address : "))
        email_password=str(getpass("Enter Senders Password : "))
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(email_address, email_password)
        print("\n\tLogin Successful!")
        break
    except:
        print("\nLogin Failed!")
        print("\nWrong Email Address or Password Retry.\n")
        print("\nNOTE: Second Attempt.")
        try:
            email_address=str(input("\nEnter Senders Email Address : "))
            email_password=str(getpass("Enter Senders Password : "))
            server=smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(email_address, email_password)
            print("\n\tLogin Successful!")
            break
        except:
            print("\nLogin Failed!")
            print("\nWrong Email Address or Password Retry.\n")
            print("\n\nNOTE: Last Attempt.")
            try:
                email_address=str(input("\nEnter Senders Email Address : "))
                email_password=str(getpass("Enter Senders Password : "))
                server=smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()
                server.login(email_address, email_password)
                print("\n\tLogin Successful!")
                break
            except:
                print("\nLogin Failed!")
                print("\nWrong Email Address or Password Retry.\n")
                print(end="Exit")
                for x in range(3):
                    print(end=".")
                    time.sleep(0.7)
                exit()

print("\n-------------------*-------------------\n")
      
while 3 :
    print("""    1. Press 1 for Sending Email to Someone.
    2. Press 2 for Viewing Sent mails.
    3. Press 3 for Opening gmail on an Browser.
    4. Press 4 for Deleting all Send Mails| OFFLINE.
    5. Press 5 for Deleting all Emails in User Inbox | ONLINE.
    6. Press 6 for Exit the Messenger.""")
    
    choice=int(input("\nEnter a choice from the above options : "))
    time.sleep(1)

    if choice == 1:
        print('\n\n--------| EMAIL SENDER |--------\n')
        
        email_receiver=str(input("Enter Receivers Email Address : "))

        def send_email(subject, msg):

            try:
                server=smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()
                server.login(email_address, email_password)
                message = 'Subject: {}\n\n{}'.format(subject, msg)
                server.sendmail(email_address, email_receiver, message)
                server.quit()
                print(end="\nSending your mail")
                for x in range(3):
                    print(end='.')
                    time.sleep(0.7)
                print('\n\nEmail was Successfully Send to ',email_receiver,'.')

            except:
                print(end="\nSending your mail to {}.".format(email_receiver))
                for x in range(3):
                    print(end='.')
                    time.sleep(0.7)
                print('\n\nEmail Failed to be Sent to ',email_receiver,'.')
        
        subject=input("Enter Email Subject : ")
        msg=input("Enter Email Content(Message) : ")

        send_email(subject, msg)

        print("\n-------------------*-------------------\n")

        if con == 'Y' or con == 'YES' or con_2 == 'N' or con_2 == 'NO':
            sql = "INSERT INTO messenger(email_address,email_receiver,Subject,content,Date_Time) VALUES (%s,%s,%s,%s,now())"
            val = (email_address, email_receiver, subject, msg)
            mycursor.execute(sql, val)
            mydb.commit()
            
            print("\n\n",mycursor.rowcount, "mail sended to ",email_receiver,"by",email_address,".")
            print("\n-------------------*-------------------\n")
    
    elif choice == 2:
        print('\n\n--------| VIEWING SENT MESSAGES |--------\n')
        if con == 'Y' or con == 'YES' or con_2 == 'N' or con_2 == 'NO':
            print(end="Fetching all emails sended till now")
            for x in range(3):
                print(end='.')
                time.sleep(0.7)
            
            sql='select * from messenger'
            mycursor.execute(sql)
            messenger = mycursor.fetchall()
            for email_address in messenger:
                print("\n\nSender's Email Address    : ", email_address[0])
                print("Receiver's Email Address  : ", email_address[1])
                print("Email Subject             : ", email_address[2])
                print("Email Content             : ", email_address[3])
                print("Email Date_time           : ", email_address[4],"\n\n")
                time.sleep(1.5)
            
            print("\nGreat, All Email(s) Caught Up...")
            print("\n-------------------*-------------------\n")

        elif con == 'N' or con == 'NO' or con_2 == 'Y' or con_2 == 'YES':
            print("\nGreat, All Email(s) Caught Up...")
            print("\n-------------------*-------------------\n")

    elif choice == 3:
        print("\n\n-------| GMAIL IN BROWSER|-------\n")
        print(end="Opening gmail")
        for x in range(3):
            print(end='.')
            time.sleep(0.7)
            
        webbrowser.open('http://gmail.com', new=7)
        
        print("\nGmail Opened in Browser...")
        print("\n-------------------*-------------------\n")

    elif choice == 4:
        print("\n\n-------| DELETING STORED EMAILS SENT TILL NOW | OFFLINE |-------\n")
        option = str(input("Confirm where you want to really delete all stored emails(Y,N) : ")).upper()
        
        if option == 'Y' or option == 'YES':
                if con == 'YES' or con == 'Y' or con_2 == 'N' or con_2 == 'NO':
                    
                    print(end='Deleting, these may take time')
                    for x in range(3):
                        print(end='.')
                        time.sleep(0.7)
                        
                    sql = "drop table messenger"
                    mycursor.execute(sql)
                    mycursor.execute("""CREATE TABLE messenger(email_address varchar(40),
                        email_receiver varchar(40),
                        Subject varchar(50),
                        content varchar(2500),
                        Date_Time varchar(30))""")
                    mydb.commit()
                    time.sleep(2)
                    print("\nTask Completed.")
                    
                    print("\n-------------------*-------------------\n")
                    
                elif con_2 == 'Y' or con_2 ==  'YES' or con == 'N' or con == 'NO':
                    print("\nNothing to go for!\n")
                    
                
        elif option == 'N' or option == 'NO':
                print(end="Continuing to Program")
                time.sleep(1)
                for x in range(3):
                    print(end='.')
                    time.sleep(0.7)
                
                print("\n-------------------*-------------------\n")
                continue
            
    elif choice == 5:
        print('\n    -----| DELETING EMAILS IN USER INBOX | ONLINE |-----\n')

        email_address=input("Users Email ID : ")
        email_passwd=str(getpass("Enter Users Password : "))
        print("\nNOTE: YOUR ALL EMAILS WILL BE DELETED FROM THE INBOX\n")
        option=str(input("Confirm where you want to really delete the mails(Y,N) : ")).upper()

        if option == 'Y' or option == 'YES':
            try:
                print(end="Searching for mails")
                for x in range(3):
                    print(end='.')
                    time.sleep(0.7)
                print("\n")
                box = imaplib.IMAP4_SSL('imap.gmail.com', 993)
                box.login(email_address, email_passwd)
                box.select('Inbox')
                typ, data = box.search(None, 'ALL')
                for num in data[0].split():
                   box.store(num, '+FLAGS', '\\Deleted')
                box.expunge()
                box.close()
                box.logout()
                print("Successfully deleted all your inbox messages.")
            except:
                print("Looks like your indox is already empty.")

        elif option == 'N' or option == 'NO':
                time.sleep(1)
                print(end="    ")
                for x in range(3):
                    print(end='.')
                    time.sleep(0.7)
                print('Continued')
                print("\n-------------------*-------------------\n")
                continue
                
        else:
            print('Invalid Entry...')
            print("\n-------------------*-------------------\n")

        print("\n-------------------*-------------------\n")
        
    elif choice == 6:
            print('\n-----| EXITING PROGRAM |-----\n')
            option=str(input("Confirm where you want to really exit(Y,N) : ")).upper()
            
            if option=='Y' or option == 'YES':
                print(end='Saving and exiting')
                for x in range(3):
                    print(end='.')
                    time.sleep(1)
                exit()
                
            elif option=='N' or option == 'NO':
                time.sleep(1)
                print(end="    ")
                for x in range(3):
                    print(end='.')
                    time.sleep(1)
                    
                print('Continued')
                print("\n-------------------*-------------------\n")
                continue
                
            else:
                print('Invalid Entry.....')
                print("\n-------------------*-------------------\n")
    else:
        print('Invalid Entry...')
        print("\n-------------------*-------------------\n")
