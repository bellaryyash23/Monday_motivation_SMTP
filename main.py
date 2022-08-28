import smtplib
import random
import datetime as dt

with open("./quotes.txt")as quotes:
    quotes_list = quotes.readlines()

now = dt.datetime.now()
day = now.weekday()

my_email = "xyz123@gmail.com"
password = "PASSWORD"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if day == 0:
        connection.sendmail(from_addr=my_email, to_addrs="abc456@yahoo.com", msg=f"Subject:Monday "
                                                                                       f"Motivation\n\nToday's "
                                                                                       f"Motivation\n"
                                                                                       f"{random.choice(quotes_list)}")
