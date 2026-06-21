def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperature_dict(temperature_dict):
    if not isinstance(temperature_dict, dict):
        raise ValueError("Input must be a dictionary")
    
    converted_temperatures = {}
    for location, temp in temperature_dict.items():
        if not isinstance(location, str):
            raise ValueError("Location keys must be strings")
        if not isinstance(temp, (int, float)):
            raise ValueError("Temperature values must be numbers")
        
        fahrenheit_temp = convert_celsius_to_fahrenheit(temp)
        converted_temperatures[location] = fahrenheit_temp
    
    return converted_temperatures

if __name__ == '__main__':
    sample_temperatures = {
        'Paris': 12,
        'Berlin': 20,
        'Madrid': 18
    }
    converted_temps = convert_temperature_dict(sample_temperatures)
    print(converted_temps)