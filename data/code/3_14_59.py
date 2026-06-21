def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError('Kelvin temperature cannot be negative')
    return kelvin - 273.15

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_kelvin_to_fahrenheit(kelvin):
    try:
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return fahrenheit
    except ValueError as e:
        print(f'Error: {e}')
        return None
if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500, -10]
    for kelvin in sample_kelvin_values:
        fahrenheit = convert_kelvin_to_fahrenheit(kelvin)
        if fahrenheit is not None:
            print(f'Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}')