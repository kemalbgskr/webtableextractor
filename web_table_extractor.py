import requests
from bs4 import BeautifulSoup
import pandas as pd

# Ganti dengan URL web target
url = "https://www.worldometers.info/world-population/population-by-country/"

# Ambil konten halaman
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Temukan elemen tabel
table = soup.find('table')

# Ambil header tabel
headers = [th.text.strip() for th in table.find_all('thead')[0].find_all('th')]

# Ambil data baris
rows = []
for row in table.find_all('tbody')[0].find_all('tr'):
    cols = [col.text.strip() for col in row.find_all('td')]
    rows.append(cols)

# Masukkan ke DataFrame
df = pd.DataFrame(rows, columns=headers)
print(df.head(100))