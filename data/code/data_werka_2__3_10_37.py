def validate_fahrenheit(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be an integer or float.")

def fahrenheit_to_kelvin(fahrenheit):
    validate_fahrenheit(fahrenheit)
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    sample_values = [0, 100, 200, 300]
    for value in sample_values:
        kelvin_value = fahrenheit_to_kelvin(value)
        print(f"{value} Fahrenheit is {kelvin_value:.2f} Kelvin")