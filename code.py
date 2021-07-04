import csv
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(start_url)

time.sleep(2)

soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find_all('table')[2]


temp_list = []
table_rows = star_table.find_all("tr")

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

# print(temp_list)

star_name = []
star_distance = []
star_mass = []
star_radius = []

for i in range(1, len(temp_list)):
    star_name.append(temp_list[i][0])   
    star_distance.append(temp_list[i][5])  
    star_mass.append(temp_list[i][8]) 
    star_radius.append(temp_list[i][9])

df2 = pd.DataFrame(list(zip(star_name, star_distance, star_mass, star_radius)), columns= ["name", "distance", "mass", "radius"])
print(df2)

df2.to_csv("dwarfstar.csv")