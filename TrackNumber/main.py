from phonenumbers import geocoder, carrier, parse
from opencage.geocoder import OpenCageGeocode
import folium

number = str(input("Input a number that you want to track: "))
p_num = parse(number)

location = geocoder.description_for_number(p_num, "en")
print(location)

# service provider
print(carrier.name_for_number(p_num, "en"))
key = "2588906a0b83445aad3756374175086a"
geocoder = OpenCageGeocode(key)

query = str(location)

results = geocoder.geocode(query)
# store latitude and longitude

lat = results[0]['geometry']['lat']
long = results[0]['geometry']['lng']

MyMap = folium.Map(location=[lat, long], zoom_start=9)

folium.Marker([lat, long], popup=location).add_to(MyMap)

# saving map in html file

MyMap.save("Location.html")
