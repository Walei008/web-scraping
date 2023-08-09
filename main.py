import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response=requests.get(URL)
website_html=response.text


soup=BeautifulSoup(website_html,"html.parser")

all_movies=soup.findAll(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

movie_titles=[movie.get_text() for movie in all_movies]
# Write your code below this line 👇
movie_order=(movie_titles[::-1])

with open("movies.txt",mode="w")as file:
    for movie in movie_order:
        file.write(f"{movie}\n")

