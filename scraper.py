import requests
from bs4 import BeautifulSoup

years_list = ["2015", "2016", "2017", "2018"]

soup_list = []

# for year in years_list:

# 	url = "https://www.baseball-reference.com/leagues/MLB/{}-schedule.shtml".format(year)

# 	response = requests.get(url)

# 	soup_list.append(BeautifulSoup(response.content, "html.parser"))

# for soup in soup_list:

url = "https://www.baseball-reference.com/leagues/MLB/2017-schedule.shtml"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

samples = soup.find_all("h3")

games = soup.find_all("p", "game")

for game in games:

	

