def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(temp_dict):
    return {location: celsius_to_fahrenheit(temp) for location, temp in temp_dict.items()}

if __name__ == '__main__':
    sample_temps = {
        'New York': 10,
        'Los Angeles': 25,
        'Chicago': 15
    }
    converted_temps = convert_temperatures(sample_temps)
    print(converted_temps)