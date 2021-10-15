from bs4 import BeautifulSoup
import requests
import pandas as pd
#pip install
url = 'https://us.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

#Obtenemos los nombres de los equipos respectivos


eq = soup.find_all('span', class_='nombre-equipo')
equipos = list()
count = 0
for i in eq:
    if count < 20:
     equipos.append(i.text)
    else:
        break
    count+=1
print(equipos)

#para obtener puntos
pt = soup.find_all('td', class_='destacado')
puntos = list()
count = 0
for i in pt:
    if count < 20:
     puntos.append(i.text)
    else:
        break
    count+=1
print(puntos)

df = pd.DataFrame({'Nombre':equipos,'Puntos':puntos},index=list(range(1,21)))
print(df)