def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be negative")
    return kelvin - 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kelvin_to_fahrenheit(kelvin):
    conversion_map = {
        'kelvin_to_celsius': lambda k: k - 273.15,
        'celsius_to_fahrenheit': lambda c: (c * 9/5) + 32
    }
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be negative")
    celsius = conversion_map['kelvin_to_celsius'](kelvin)
    fahrenheit = conversion_map['celsius_to_fahrenheit'](celsius)
    return fahrenheit

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    for kelvin in sample_kelvin_values:
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")