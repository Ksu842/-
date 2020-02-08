import requests
from bs4 import BeautifulSoup

silkar = []
nomer = input("Введите номер задачи: ")
silka = requests.get('https://gdz.ru/class-6/matematika/dorofeev-sharygin/'+ nomer + '-nom/')

soup = BeautifulSoup(silka.content, "html.parser")
images = soup.findAll('img')

for i in images:
    if "tasks" in i.get('src'):
        silkar.append(i.get('src'))


