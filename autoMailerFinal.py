#This program iterates through a list to send multiple emails of the same format. 

import smtplib
from email.message import EmailMessage

#email server settings
email_server = 'server_address' #enter your email server here e.g. smtp.gmail.com 
port = 465 #this is the usual value but it can vary depending on security
sender = 'your_email' #enter your email address here
key = 'your_password' #enter your email password here

#initialize list variables
body,emails,givers,getters = []
subject = 'Christmas Grab Bag Victiim'

#pull email addresses and lists of names from a file.
#I used csv as it's easiest to split and clean. It's also easiest manipulate the
# 'random' list of names in a spreadsheet.
with open("GrabBagList.csv") as f:
    for line in f:
        data = line.split(',')
        #print(data) #debug line to test file reading
        emails.append(data[0])
        givers.append(data[1])
        getters.append(data[2].strip()) #.strip() method to remove newlines

#more debug statements
# print(emails)
# print(givers)
# print(getters)

#create a list of tuples (of strings) - easier to iterate
people = list(zip(emails,givers,getters))
# print(people) # more debugging


server = smtplib.SMTP_SSL(email_server,port) #create SMTP server object
server.login(sender,key) #login to server
#This loop creates and sends the emails using the EmailMessage class.
#This was used because it's easier to specify the header info than the more general
#Message class.
for email,giver,getter in people:
	msg = EmailMessage()
	msg.set_content('{}, you buy for {}!'.format(giver,getter))
	msg['Subject'] = 'Christmas Grabbag Victim'
	msg['From'] = sender
	msg['To'] = email
	server.send_message(msg)
server.quit()