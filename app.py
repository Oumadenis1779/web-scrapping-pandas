import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

movies = []
for row in soup.select("tbody.lister-list tr"):
    title = row.find('td', class_='titleColumn').find('a').get_text()
    year = row.find('td', class_='titleColumn').find('span', class_='secondaryInfo').get_text()[1:-1]
    rating = row.find('td', class_='ratingColumn imdbRating').find('strong').get_text()
    movies.append([title, year, rating])

# Store the information in a pandas dataframe
df = pd.DataFrame(movies, columns=['Title', 'Year', 'Rating'])

# Add a delay between requests to avoid overwhelming the website with requests
time.sleep(1)

# Save dataframe to a CSV file
df.to_csv('top-rated-movies.csv', index=False)
