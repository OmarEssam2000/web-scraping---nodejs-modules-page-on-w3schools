#1st step install and import modules
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
module = []
description = []

#2nd step use requests to fetch the url
result = requests.get("https://www.w3schools.com/nodejs/ref_modules.asp")
#3rd step save page content/markup
src = result.content
#4th step create soup object to parse content
soup = BeautifulSoup(src , "lxml")
#5th step find the elements containing info we need
#-- job titles, job skills, company names, location names الحاجات اللى احنا عايزينها
table1 = soup.find("table" , {"class":"ws-table-all"})


#6th step loop over returned lists to extract needed info into other lists
for i in table1.find_all('tr'):
    store1 = i.select_one('td:nth-child(1)')
    if store1 is not None:
        module.append(store1.text)
print(module)

for i in table1.find_all('tr'):
    store2 = i.select_one('td:nth-child(2)')
    if store2 is not None:
        description.append(store2.text)
print(description)


#7th step create csv file and fill it with values
file_list = [module , description]
exported = zip_longest(*file_list) #دي الفانكشن اللى بتجيب واحد من كل ليسته جنب بعض 
filepath = "E:/programming/web scraping/wuzuf website/filgoal.csv"
with open(filepath , "w" , encoding='utf-8' ) as myfile :
    wr = csv.writer(myfile)
    wr.writerow(["Module" , "Description"])
    wr.writerows(exported)