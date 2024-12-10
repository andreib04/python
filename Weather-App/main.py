from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x650+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="abcd")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat = location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text = "Current Weather")

        #weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fa326244f16991608c3311179445534f"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text = (temp, "°C"))
        c.config(text = (condition, "|", "Feels", "Like", temp,"°C"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text = pressure) 
    
    except Exception as e:
        messagebox.showerror("Weather", "Invalid city name!")

#search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x = 200, y = 20)

textfield = tk.Entry(root, justify="center", width=20, font=("Poppins", 25), bg="#404040", border=0, fg="white")
textfield.place(x = 250, y = 40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command = getWeather)
myimage_icon.place(x = 582, y = 34)

#logo
Logo_image=PhotoImage(file="logo.png")
logo = Label(image = Logo_image)
logo.place(x = 250, y = 100)

#bottom box
frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image = frame_image)
frame_myimage.pack(padx = 5, pady = 5, side=BOTTOM)

#time
name = Label(root, font=("arial", 15, "bold"))
name.place(x = 30, y = 150)
clock = Label(root, font = ("Poppins", 20))
clock.place(x = 30, y = 180)

#label
label1 = Label(root, text = "Wind", font=("Poppins", 15, 'bold'), fg="white", bg = "#1ab5ef")
label1.place(x = 120, y = 548)

label2 = Label(root, text = "Humidity", font=("Poppins", 15, 'bold'), fg="white", bg = "#1ab5ef")
label2.place(x = 250, y = 548)

label3 = Label(root, text = "Description", font=("Poppins", 15, 'bold'), fg="white", bg = "#1ab5ef")
label3.place(x = 430, y = 548)

label4 = Label(root, text = "Pressure", font=("Poppins", 15, 'bold'), fg="white", bg = "#1ab5ef")
label4.place(x = 650, y = 548)


t = Label(font=("arial", 70), fg="#ee666d")
t.place(x = 650, y = 140)
c = Label(font=("arial", 15))
c.place(x = 650, y = 240)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x = 120, y = 570)

h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x = 250, y = 570)

d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x = 430, y = 570)

p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x = 650, y = 570)

root.mainloop()