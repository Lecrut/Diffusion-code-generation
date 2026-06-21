def validate_kelvin(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be negative")

def convert_kelvin_to_celsius(kelvin):
    validate_kelvin(kelvin)
    return kelvin - 273.15

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_kelvin_to_fahrenheit(kelvin):
    celsius = convert_kelvin_to_celsius(kelvin)
    return convert_celsius_to_fahrenheit(celsius)

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    for kelvin in sample_kelvin_values:
        fahrenheit = convert_kelvin_to_fahrenheit(kelvin)
        print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")