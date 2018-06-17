import smtplib
from time import gmtime, strftime
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("your email", "your password")
fin=("Login Detected at ")
tim=strftime("%Y-%m-%d %H:%M:%S", gmtime())
final=fin+tim
s.sendmail("your email", "send email to", final)
s.quit()