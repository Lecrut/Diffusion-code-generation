def celsius_to_fahrenheit(readings):
    return {location: temp * 9 / 5 + 32 for location, temp in readings.items()}

if __name__ == '__main__':
    sample_data = {
        "New York": 25.0,
        "London": 18.5,
        "Tokyo": 30.0,
        "Sydney": 15.2
    }
    result = celsius_to_fahrenheit(sample_data)
    print(result)