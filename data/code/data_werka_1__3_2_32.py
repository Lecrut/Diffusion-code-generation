def convert_celsius_to_fahrenheit(celsius_dict):
    fahrenheit_dict = {}
    for location, celsius in celsius_dict.items():
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_dict[location] = fahrenheit
    return fahrenheit_dict

if __name__ == '__main__':
    sample_temperatures = {
        'New York': 10,
        'Los Angeles': 25,
        'Chicago': -5,
        'Houston': 30
    }
    
    converted_temperatures = convert_celsius_to_fahrenheit(sample_temperatures)
    print(converted_temperatures)