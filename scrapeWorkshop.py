#import libraries 

from bs4 import BeautifulSoup
import urllib.request
import csv

# specify the url
urlpage =  'https://en.wikipedia.org/wiki/List_of_best-selling_video_games'

# query the website and return the html to the variable 'page'
try:
    page = urllib.request.urlopen(urlpage)
except urllib.error.URLError as e:
    print(e.reason)

#print(page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

#print(soup)

# find results within table
table = soup.find('table', attrs={'class': 'wikitable plainrowheaders sortable'})
print("Starting scrape....")
#print(table)
results = table.find_all('tr')
print('Number of results', len(results))

# create and write headers to a list 
rows = []
rows.append(['Number','Title', 'Sales', 'Platform(s) ', 'Release Date', 'Developer(s)', 'Publisher(s)'])
#print(rows)

# loop over results
num = 1
for result in results:
    # find all columns per result
    data = result.find_all('td')
    # check that columns have data 
    if len(data) == 0: 
        continue

# write columns to variables
    Title = data[0].getText().replace("\n",",").strip("\",\"")
    Sales = data[1].getText().replace("\n",",").strip("\",\"")
    Platforms = data[2].getText().replace("\n",",").strip("\",\"")
    Release_Date = data[3].getText().replace("\n",",").strip("\",\"")
    Developers = data[4].getText().replace("\n",",").strip("\",\"")
    Publishers = data[5].getText().replace("\n",",").strip("\",\"")
    

    # write each result to rows
    rows.append([num,Title, Sales, Platforms, Release_Date, Developers, Publishers])
    #print(rows)
    num+=1
    #print("\n")

    # Create csv and write rows to output file
    with open('wikiScrape.csv','w', newline='') as f_output:
        csv_output = csv.writer(f_output)
        csv_output.writerows(rows)
print("Done scraping, check CSV for output")
