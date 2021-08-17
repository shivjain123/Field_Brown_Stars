import pandas as pd
from bs4 import BeautifulSoup
import time
import requests as req

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = req.get(url)

time.sleep(5)

name_list = list()
distance_list = list()
mass_list = list()
radius_list = list()

soup = BeautifulSoup(page.text, "html.parser")
table = soup.find_all("table")
tbody = table[7].find_all("tr")

temp_list=[]

for tr_tags in tbody:
    td_tags = tr_tags.find_all("td")
    row = [i.text.rstrip() for i in td_tags]
    temp_list.append(row)

    print(temp_list[0])

for i in range(1,len(temp_list)):
    
    name_list.append(temp_list[i][0])
    distance_list.append(temp_list[i][5])
    mass_list.append(temp_list[i][7])
    radius_list.append(temp_list[i][8])

df = pd.DataFrame(list(zip(name_list, distance_list, mass_list, radius_list)), columns = ["Name", "Distance", "Mass", "Radius"])
print(df)
df.to_csv('D:/(4) WhiteHatJr/Third Module/Web Scraping/Stars/brown.csv')