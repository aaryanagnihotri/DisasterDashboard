
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
# Example: Replace with your real model outputs
earthquake_data = pd.DataFrame({
    "Latitude": [28.6, 26.9, 12.9],
    "Longitude": [77.2, 85.3, 77.6],
    "Risk": ["HIGH RISK", "NORMAL", "HIGH RISK"]
})

flood_data = pd.DataFrame({
    "Latitude": [25.6, 22.9, 20.9],
    "Longitude": [88.3, 80.3, 75.6],
    "Risk": ["NORMAL", "HIGH RISK", "NORMAL"]
})

heatwave_data = pd.DataFrame({
    "Latitude": [30.7, 23.2, 19.1],
    "Longitude": [76.8, 81.3, 72.9],
    "Risk": ["HIGH RISK", "NORMAL", "NORMAL"]
})

rainfall_data = pd.DataFrame({
    "Latitude": [24.7, 27.5, 21.2],
    "Longitude": [84.0, 78.2, 73.9],
    "Risk": ["NORMAL", "HIGH RISK", "NORMAL"]
})

weather_data = pd.DataFrame({
    "Latitude": [28.6, 17.4, 22.1],
    "Longitude": [77.2, 78.5, 75.1],
    "Risk": ["NORMAL", "HIGH RISK", "NORMAL"]
})

landslide_data = pd.DataFrame({
    "Latitude": [27.1, 31.1, 22.6],
    "Longitude": [88.6, 77.1, 82.5],
    "Risk": ["HIGH RISK", "NORMAL", "NORMAL"]
})

drought_data = pd.DataFrame({
    "Latitude": [18.5, 21.1, 25.4],
    "Longitude": [73.8, 77.3, 79.2],
    "Risk": ["NORMAL", "HIGH RISK", "NORMAL"]
})
import folium

def make_disaster_map(data, disaster_name, save_path):
    m = folium.Map(location=[22.9734, 78.6569], zoom_start=5)
    
    for _, row in data.iterrows():
        color = "red" if row["Risk"] == "HIGH RISK" else "green"
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=8,
            popup=f"{disaster_name} - {row['Risk']}",
            color=color,
            fill=True,
            fill_color=color
        ).add_to(m)
    
    m.save(save_path)
    print(f"✅ {disaster_name} map saved: {save_path}")
make_disaster_map(earthquake_data, "Earthquake", "earthquake_map.html")
make_disaster_map(flood_data, "Flood", "flood_map.html")
make_disaster_map(heatwave_data, "Heatwave", "heatwave_map.html")
make_disaster_map(rainfall_data, "Rainfall", "rainfall_map.html")
make_disaster_map(weather_data, "Weather", "weather_map.html")
make_disaster_map(landslide_data, "Landslide", "landslide_map.html")
make_disaster_map(drought_data, "Drought", "drought_map.html")
def disaster_alerts(data, disaster_name):
    alerts = []
    for _, row in data.iterrows():
        if row["Risk"] == "HIGH RISK":
            alerts.append(f"⚠️ ALERT: {disaster_name} risk near ({row['Latitude']}, {row['Longitude']})")
    return alerts

all_alerts = []
all_alerts += disaster_alerts(earthquake_data, "Earthquake")
all_alerts += disaster_alerts(flood_data, "Flood")
all_alerts += disaster_alerts(heatwave_data, "Heatwave")
all_alerts += disaster_alerts(rainfall_data, "Rainfall")
all_alerts += disaster_alerts(weather_data, "Weather")
all_alerts += disaster_alerts(landslide_data, "Landslide")
all_alerts += disaster_alerts(drought_data, "Drought")

print("\n".join(all_alerts) if all_alerts else "✅ All regions safe")
