def convert_celsius_to_fahrenheit(temperature_readings):
    return {location: (celsius * 9 / 5) + 32 for location, celsius in temperature_readings.items()}

if __name__ == '__main__':
    sample_readings = {
        'New York': 20.0,
        'London': 15.5,
        'Tokyo': 25.0,
        'Sydney': 30.0
    }
    result = convert_celsius_to_fahrenheit(sample_readings)
    print(result)