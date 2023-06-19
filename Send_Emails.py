#SendEmails
#uses module index.html
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Anthony Sandoval'
email['to'] = 'sandovalanthony0114@gmail.com'
email['subject'] = 'You Won 1,000,000 dollars!'

email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jellyfin.moviebox@gmail.com', 'zawc wgun dhhg yszi')
    smtp.send_message(email)
    print('all good boss!')

