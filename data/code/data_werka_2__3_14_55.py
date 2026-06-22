def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be negative")
    return kelvin - 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

if __name__ == '__main__':
    sample_kelvin_values = [100, 273.15, 400, 600]
    for kelvin in sample_kelvin_values:
        fahrenheit = convert_kelvin_to_fahrenheit(kelvin)
        print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")