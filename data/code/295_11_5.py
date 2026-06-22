temp_conversions = {
    'CtoF': lambda c: (c * 9/5) + 32,
    'FtoC': lambda f: (f - 32) * 5/9
}

def convert_temperature(value, from_scale, to_scale):
    if from_scale not in temp_conversions or to_scale not in temp_conversions:
        raise ValueError("Invalid scale provided")
    
    converter = temp_conversions[f"{from_scale}to{to_scale}"]
    return converter(value)

if __name__ == '__main__':
    celsius_value = 25.0
    fahrenheit_value = convert_temperature(celsius_value, 'C', 'F')
    print(f"{celsius_value} C is {fahrenheit_value:.2f} F")

    fahrenheit_value = 77.0
    celsius_value = convert_temperature(fahrenheit_value, 'F', 'C')
    print(f"{fahrenheit_value} F is {celsius_value:.2f} C")