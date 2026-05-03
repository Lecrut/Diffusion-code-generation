def celsius_to_fahrenheit(readings):
    fahrenheit_readings = {}
    for location, celsius in readings.items():
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_readings[location] = fahrenheit
    return fahrenheit_readings
if __name__ == '__main__':
    sample_readings = {
        "London": 15.0,
        "New York": 22.5,
        "Tokyo": 28.0,
        "Sydney": 30.0
    }
    converted_readings = celsius_to_fahrenheit(sample_readings)
    print(converted_readings)