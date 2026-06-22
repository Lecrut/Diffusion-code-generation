def validate_fahrenheit(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Temperature must be a number.")
    return value

def fahrenheit_to_kelvin(fahrenheit):
    validated_value = validate_fahrenheit(fahrenheit)
    kelvin = (validated_value - 32) * 5 / 9 + 273.15
    return kelvin

if __name__ == '__main__':
    sample_values = [0, 68, 100, 37]
    for value in sample_values:
        try:
            kelvin_value = fahrenheit_to_kelvin(value)
            print(f"{value} Fahrenheit is {kelvin_value:.2f} Kelvin")
        except ValueError as e:
            print(e)