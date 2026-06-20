def celsius_to_fahrenheit(readings):
    return {location: temp * 9 / 5 + 32 for location, temp in readings.items()}

if __name__ == '__main__':
    sample_data = {
        "New York": 22.5,
        "London": 18.0,
        "Tokyo": 30.0,
        "Sydney": 15.5
    }
    converted_readings = celsius_to_fahrenheit(sample_data)
    print(converted_readings)