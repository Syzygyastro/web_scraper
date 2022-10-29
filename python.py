""" sample Script for axtracting Data from a Webpage 
This script allows the user to exact data from a webapge and then export the data to a csv file with column(s).
"""
# libraries
import urllib.request
from bs4 import BeautifulSoup
import csv
# Put your URL here
url = 'https://www.nytimes.com/books/best-sellers/combined-print-and-e-book-nonfiction/'
# Fetching the html
request = urllib.request.Request(url)
content = urllib.request.urlopen(request)
# Parsing the html 

# Provide html elements' attributes to extract the data 
text1 = parse.find_all('h3', attrs={'class': 'css-5pe77f'})
text2 = parse.find_all('p', attrs={'class': 'css-hjukut'})
# Writing extracted data in a csv file
  writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  writer.writerow(['Title','Author'])
  for col1,col2 in zip(text1, text2):
    writer.writerow([col1.get_text().strip(), col2.get_text().strip()])

# parsing html using BeautifulSoup
soup = bs4(content, 'html.parser')
print(soup.title)
print(soup.title.name)

#finding elements by id or by class
s = soup.find('div', class_='css-5pe77f')
soupContentClass = s.find_all('p')
soupContentId = s.find('div', id='css-5zg4y9')
print(f`${soupContentClass:} {soupContentId:}`)


#extracting text from tags
s = soup.find('div', class_='css-1dv1kvn')
 
lines = s.find_all('h2')
 
for line in lines:
    print(line.text)

#extract href links
# find all the anchor tags with "href"
for link in soup.find_all('a'):
    print(link.get('href'))

#Extract image from img tags
images_list = []
 
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})
     
for image in images_list:
    print(image)