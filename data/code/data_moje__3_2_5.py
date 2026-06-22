def celsius_to_fahrenheit(temperature_dict):
    return {key: (value * 9 / 5) + 32 for key, value in temperature_dict.items()}

if __name__ == '__main__':
    sample_temperatures = {
        "New York": 20,
        "London": 15,
        "Tokyo": 25,
        "Sydney": 30
    }
    converted_temperatures = celsius_to_fahrenheit(sample_temperatures)
    print(converted_temperatures)