def celsius_to_fahrenheit(temperatures):
    return {location: (celsius * 9 / 5) + 32 for location, celsius in temperatures.items()}

if __name__ == '__main__':
    sample_readings = {
        "New York": 10.5,
        "London": 8.0,
        "Tokyo": 22.3
    }
    fahrenheit_readings = celsius_to_fahrenheit(sample_readings)
    print(fahrenheit_readings)