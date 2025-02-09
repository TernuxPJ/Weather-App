import tkinter as tk
from tkinter import messagebox
import requests
from tkinter import Toplevel, Label, Button

API_KEY = "Your-API"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

root = tk.Tk()
root.title("Weather App")
root.geometry("800x600")
root.configure(bg="#2c3e50")

title_font = ("Montserrat", 26, "bold")
label_font = ("Montserrat", 14)
button_font = ("Montserrat", 16, "bold")
result_font = ("Montserrat", 16)

def get_weather():
    city = city_input.get().strip()
    if not city:
        messagebox.showwarning("Error", "Please enter a city name!")
        return
    
    complete_url = f"{BASE_URL}appid={API_KEY}&q={city}"
    response = requests.get(complete_url)
    data = response.json()

    if data.get("cod") != 200:
        messagebox.showerror("Error", "City not found!")
        return
    
    city_name = data["name"]
    country = data["sys"]["country"]
    temp = round(data["main"]["temp"] - 273.15, 1)
    feels_like = round(data["main"]["feels_like"] - 273.15, 1)
    weather = data["weather"][0]["description"].capitalize()
    min_temp = round(data["main"]["temp_min"] - 273.15, 1)
    max_temp = round(data["main"]["temp_max"] - 273.15, 1)

    message = (
        f"{city_name}, {country}\n\n"
        f"Temperature: {temp}°C\n"
        f"Feels Like: {feels_like}°C\n"
        f"Weather: {weather}\n"
        f"Min Temp: {min_temp}°C  |  Max Temp: {max_temp}°C"
    )

    show_weather_message("Weather Information", message, button_color="#3498db")

def show_weather_message(title, message, button_color="#3498db"):
    msg_window = Toplevel(root)
    msg_window.title(title)
    msg_window.geometry("500x300")
    msg_window.configure(bg="#ecf0f1")
    msg_window.resizable(False, False)

    frame = tk.Frame(msg_window, bg="#ecf0f1", padx=40, pady=30)
    frame.pack(fill="both", expand=True)

    message_label = Label(frame, text=message, font=("Roboto", 16), bg="#ecf0f1", fg="#2c3e50", justify="center")
    message_label.pack(pady=20)





frame = tk.Frame(root, bg="#34495e", relief="flat", bd=0, padx=40, pady=40)
frame.place(relx=0.5, rely=0.5, anchor="center")

title_label = tk.Label(frame, text="Weather App", font=title_font, fg="#ecf0f1", bg="#34495e")
title_label.grid(row=0, column=0, columnspan=2, pady=40)

city_label = tk.Label(frame, text="Enter City:", font=label_font, fg="#ecf0f1", bg="#34495e")
city_label.grid(row=1, column=0, padx=15, pady=10, sticky="w")

city_input = tk.Entry(frame, font=("Montserrat", 16), bd=0, relief="solid", width=35,
                      fg="#ecf0f1", bg="#2c3e50", insertbackground="white", justify="center")
city_input.grid(row=1, column=1, padx=15, pady=10)

search_button = tk.Button(frame, text="Get Weather", font=button_font, bg="#1abc9c", fg="white", bd=0,
                          relief="flat", width=20, height=2, command=get_weather)
search_button.grid(row=2, column=0, columnspan=2, pady=30)

def on_enter(e):
    search_button['bg'] = "#16a085"

def on_leave(e):
    search_button['bg'] = "#1abc9c"

search_button.bind("<Enter>", on_enter)
search_button.bind("<Leave>", on_leave)

root.mainloop()
