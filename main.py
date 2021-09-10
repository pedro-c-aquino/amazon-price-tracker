from bs4 import BeautifulSoup
import requests
from smtplib import SMTP

# Constants set to track the product price

URL = "https://www.amazon.com.br/Assassins-Creed-Valhalla-Limitada-PlayStation/dp/B08KJY5RG6/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2LBHXUNRVL5KU&dchild=1&keywords=assassins+creed+valhalla&qid=1621628491&sprefix=assassin%2Caps%2C311&sr=8-1"

PRICE = 100

MY_EMAIL = # enter your email

PASSWORD = # enter your password

# Headers for the request

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6,fr;q=0.5"

}

# Make the request and parse the response with Beautiful Soup
response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

price_tag = soup.find(name="span", id="priceblock_ourprice", class_="a-size-medium a-color-price priceBlockBuyingPriceString")

price_str = price_tag.get_text()

# Edit the price to compare with your wanted price

price_edited_1 = price_str.replace("R$", "")
price_edited_2 = round(float(price_edited_1.replace(",", ".")), 2)

# Compare prices and send an email if the price is below your target
if price_edited_2 < PRICE:
    message = f"Assassin's creed Valhala is with a {price_edited_2} price."
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=# target email, msg=message)
