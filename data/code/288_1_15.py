def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be a number")
    return temp

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return (celsius * 9/5) + 32

def convert_temp(temp, source_scale):
    temp = validate_temperature(temp)
    
    if source_scale == "Kelvin":
        results = {
            "Celsius": kelvin_to_celsius(temp),
            "Fahrenheit": kelvin_to_fahrenheit(temp),
            "Rankine": (temp * 9/5)
        }
    else:
        raise ValueError("Unsupported source scale")
    
    return results

if __name__ == '__main__':
    test_cases = [
        (273.15, "Kelvin"),
        (0, "Kelvin"),
        (373.15, "Kelvin")
    ]
    
    for temp, scale in test_cases:
        print(convert_temp(temp, scale))