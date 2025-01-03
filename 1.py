# Simulated weather data for demonstration purposes
weather_data = {
    "Gujarat": {"Temperature": 22, "Pressure": 1012, "Humidity": 60, "Description": "Clear sky"},
    "Manali": {"Temperature": 15, "Pressure": 1008, "Humidity": 75, "Description": "Light rain"},
    "Rajasthan": {"Temperature": 28, "Pressure": 1010, "Humidity": 50, "Description": "Sunny"},
    "Mumbai": {"Temperature": 30, "Pressure": 1005, "Humidity": 85, "Description": "Humid"},
}

# Function to display weather data
def display_weather(city):
    if city in weather_data:
        data = weather_data[city]
        print(f"Weather in {city}:")
        print(f"Temperature: {data['Temperature']} °C")
        print(f"Pressure: {data['Pressure']} hPa")
        print(f"Humidity: {data['Humidity']} %")
        print(f"Description: {data['Description']}")
    else:
        print("City not found in the simulated dataset.")

# Main function to run the program
if __name__ == "__main__":
    city_name = input("Enter city name (e.g., Gujarat, Manali, Rajasthan, Mumbai): ")
    display_weather(city_name)
