def convert_celsius_to_fahrenheit(temperatures):
    return {location: (temp * 9 / 5) + 32 for location, temp in temperatures.items()}

if __name__ == '__main__':
    sample_temperatures = {
        "New York": 20.0,
        "London": 15.0,
        "Tokyo": 25.0,
        "Sydney": 30.0
    }
    result = convert_celsius_to_fahrenheit(sample_temperatures)
    print(result)