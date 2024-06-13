import requests
from bs4 import BeautifulSoup as bs
import colorama

colorama.init()

url = f"https://www.binance.com/ru/markets/overview?p=1"
r = requests.get(url)

soup = bs(r.text, 'lxml')
name_soup = soup.find_all("div", class_="css-1ydqfmf")

print(f"{colorama.Fore.LIGHTCYAN_EX}Название - Цена: Рост - Капитализация{colorama.Fore.LIGHTWHITE_EX}")
for i in name_soup:
    name = i.find("div", class_="subtitle3 text-t-primary css-vurnku").text
    price = i.find("div", class_="body2 items-center css-18yakpx").text
    a = i.find("div", class_="subtitle3 css-18jvuxg") #-
    b = i.find("div", class_="subtitle3 css-191zdd8") #+
    capitalizetion = i.find("div", class_="body2 text-t-primary css-18yakpx").text
    q = str(a.text) if a is not None else str(b.text)
    print(f"{name} - {price}: {colorama.Fore.LIGHTRED_EX if a is not None else colorama.Fore.LIGHTGREEN_EX}{q}{colorama.Fore.LIGHTWHITE_EX} - {capitalizetion}")


