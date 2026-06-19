def convert_celsius_to_fahrenheit(temperature_dict):
    return {location: (celsius * 9/5) + 32 for location, celsius in temperature_dict.items()}

if __name__ == '__main__':
    sample_temperatures = {
        'New York': 10,
        'Los Angeles': 25,
        'Chicago': 15
    }
    converted_temperatures = convert_celsius_to_fahrenheit(sample_temperatures)
    print(converted_temperatures)