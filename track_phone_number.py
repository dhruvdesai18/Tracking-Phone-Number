import phonenumbers
from phonenumbers import geocoder
import folium
from phonenumbers import carrier

from opencage.geocoder import OpenCageGeocode

number = input("Enter Phone Number (include country code): ")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

key = "9ce54fe1c5f841b5bda9bd4883170af2"
geocoder = OpenCageGeocode(key)

query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,",", lng)

map_location = folium.Map(location = [lat,lng], zoom_start = 10)
folium.Marker([lat,lng], popup = number_location).add_to(map_location)
map_location.save("mylocation.html")

