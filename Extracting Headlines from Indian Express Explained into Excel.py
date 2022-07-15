
"""
Created on Mon Jul 11 17:44:42 2022

@author: BIPLOB GON
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
response = requests.get('https://indianexpress.com/section/explained/')
html = BeautifulSoup(response.text, 'lxml')
data = html.find ('body')
headlines = data.find_all ('h3')

print('The IE-Explained')
df = pd.DataFrame(columns=['Headline number', 'Headline'])
i = 1
for news in headlines:
    print(f"HeadlineNo{i}: ",
    news.text.strip())
    df=df.append({'Headline Number' : f"HeadlineNo {i}: ", 'Headline':news.text.strip()},
    ignore_index=True)
    i+=1
print ("End of List")
df.to_excel("The Indian Express - Explained Headlines.xlsx", index=False)
print("Excel file created") 