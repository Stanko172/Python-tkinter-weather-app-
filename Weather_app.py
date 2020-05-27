import tkinter as tk
from tkinter import font
import requests

HEIGHT = 600
WIDTH = 500

def get_weather(city):
    weather_key = 'c2dc41d1a6f5bdf54ef7f542c5e16a92'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']

        label['text'] = 'City: %s \n Description: %s  \n Temp: %s' % (name, description, temp)
    
    except:
        
        label['text'] = 'Dogodila se neka greška!'
        

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background_image.png')
background_label = tk.Label(root, image= background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#6ca0f5", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor="n")

entry = tk.Entry(frame, bg="lightgrey", font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Click me", command= lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth= 0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#6ca0f5", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=('Berlin Sans FB', 18))
label.place(relwidth=1, relheight=1)

root.mainloop()
