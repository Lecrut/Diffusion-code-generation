def celsius_to_fahrenheit(celsius_readings):
    fahrenheit_readings = {}
    for location, celsius in celsius_readings.items():
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_readings[location] = fahrenheit
    return fahrenheit_readings
if __name__ == '__main__':
    sample_data = {
        "London": 15.0,
        "New York": 22.5,
        "Tokyo": 28.0,
        "Dubai": 40.0
    }
    converted_data = celsius_to_fahrenheit(sample_data)
    print(converted_data)