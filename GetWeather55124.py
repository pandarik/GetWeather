import requests

url = "http://api.openweathermap.org/data/2.5/weather?appid=95f67b2dc5f2ff23c434f645bdbd4c04&zip="

ZipCode = input("Enter Zip Code: ")
url += ZipCode

data = requests.get(url).json()

Temp = data.get('main')
Temp = Temp.get('temp')

TempF = (Temp-273.15)*(9/5)+32
TempF = round(TempF,2)

#print(data)
print(data.get("name") + ":" + str(TempF) + "F")