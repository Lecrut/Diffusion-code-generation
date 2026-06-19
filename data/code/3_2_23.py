def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(temperature_dict):
    return {location: celsius_to_fahrenheit(temp) for location, temp in temperature_dict.items()}

if __name__ == '__main__':
    sample_temperatures = {
        'New York': 0,
        'London': 15,
        'Tokyo': 25,
        'Sydney': 30
    }
    
    converted_temperatures = convert_temperatures(sample_temperatures)
    print(converted_temperatures)