def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a number")
    return (celsius * 9/5) + 32

def convert_temperatures(temperature_dict):
    if not isinstance(temperature_dict, dict):
        raise ValueError("Input must be a dictionary")
    
    converted_dict = {}
    for location, temp in temperature_dict.items():
        if not isinstance(location, str):
            raise ValueError("Location keys must be strings")
        if not isinstance(temp, (int, float)):
            raise ValueError("Temperature values must be numbers")
        
        converted_temp = celsius_to_fahrenheit(temp)
        converted_dict[location] = converted_temp
    
    return converted_dict

if __name__ == '__main__':
    sample_temperatures = {
        'Paris': 20,
        'London': 15,
        'Berlin': 18
    }
    try:
        converted_temperatures = convert_temperatures(sample_temperatures)
        print(converted_temperatures)
    except ValueError as e:
        print(f"Error: {e}")