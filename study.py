print("//-// (()) P E from hackpy (:")
import urllib.request
from bs4 import BeautifulSoup
page=urllib.request.urlopen('https://ktu.edu.in/')
soup=BeautifulSoup(page, features='html.parser')
note=soup.find(class_='annuncement')
dep=note.find_all('a')
for deeper in dep:
	hackpy= '>>'+deeper.contents[0]
	print(hackpy)

		   