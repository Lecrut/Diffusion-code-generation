def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def validate_temperature_dict(temperature_dict):
    if not isinstance(temperature_dict, dict):
        raise ValueError("Input must be a dictionary")
    for location, temp in temperature_dict.items():
        if not isinstance(location, str):
            raise ValueError("Location keys must be strings")
        if not isinstance(temp, (int, float)):
            raise ValueError("Temperature values must be numbers")

def convert_temperatures(temperature_dict):
    validate_temperature_dict(temperature_dict)
    return {location: convert_celsius_to_fahrenheit(temp) for location, temp in temperature_dict.items()}

if __name__ == '__main__':
    sample_temperatures = {
        'Paris': 5,
        'London': 10,
        'Berlin': 8
    }
    try:
        converted_temperatures = convert_temperatures(sample_temperatures)
        print(converted_temperatures)
    except ValueError as e:
        print(e)