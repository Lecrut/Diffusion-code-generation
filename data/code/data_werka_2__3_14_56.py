def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be negative")
    return kelvin - 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_kelvin_to_fahrenheit(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be negative")
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    for kelvin in sample_kelvin_values:
        try:
            fahrenheit = convert_kelvin_to_fahrenheit(kelvin)
            print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")
        except ValueError as e:
            print(e)