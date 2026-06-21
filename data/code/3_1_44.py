def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(temperature_dict):
    conversion_function = {
        'Celsius': celsius_to_fahrenheit
    }
    
    if not isinstance(temperature_dict, dict):
        raise ValueError("Input must be a dictionary")
    
    converted_dict = {}
    for location, temp_data in temperature_dict.items():
        if not isinstance(location, str):
            raise ValueError("Location keys must be strings")
        
        unit = temp_data.get('unit', 'Celsius')
        temp_value = temp_data['value']
        
        if not isinstance(temp_value, (int, float)):
            raise ValueError("Temperature values must be numbers")
        
        if unit not in conversion_function:
            raise ValueError(f"Unsupported temperature unit: {unit}")
        
        converted_temp = conversion_function[unit](temp_value)
        converted_dict[location] = {
            'value': converted_temp,
            'unit': 'Fahrenheit'
        }
    
    return converted_dict

if __name__ == '__main__':
    sample_temperatures = {
        'London': {'value': 5, 'unit': 'Celsius'},
        'Paris': {'value': 10, 'unit': 'Celsius'},
        'Berlin': {'value': 3, 'unit': 'Celsius'}
    }
    
    converted_temperatures = convert_temperatures(sample_temperatures)
    print(converted_temperatures)