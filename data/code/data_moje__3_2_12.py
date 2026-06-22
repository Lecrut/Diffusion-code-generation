def celsius_to_fahrenheit(temperatures):
    return {location: (temp * 9 / 5) + 32 for location, temp in temperatures.items()}

if __name__ == '__main__':
    sample_temperatures = {"New York": 10, "London": 15, "Tokyo": 20}
    result = celsius_to_fahrenheit(sample_temperatures)
    print(result)