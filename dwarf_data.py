from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

dwarf_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(dwarf_url)
soup = bs(page.text,"html.parser")

star_table = soup.find('table')
temp_list = []
table_rows = star_table[2].find_all("tr")

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_names = []
distance = []
mass = []
radius = []

print(temp_list)

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][6])
    mass.append(temp_list[i][9])
    radius.append(temp_list[i][10])

headers = ["star_names","distance","mass","radius"]
df = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns = headers)
df.to_csv('dwarf_stars.csv')