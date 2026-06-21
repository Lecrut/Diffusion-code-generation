KELVIN_TO_CELSIUS_OFFSET = 273.15
CELSIUS_TO_FAHRENHEIT_MULTIPLIER = 9/5
FAHRENHEIN_ADDENDUM = 32

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be negative")
    return kelvin - KELVIN_TO_CELSIUS_OFFSET

def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_MULTIPLIER) + FAHRENHEIN_ADDENDUM

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

if __name__ == '__main__':
    sample_kelvin_values = [0, 100, 273.15, 373.15]
    for kelvin in sample_kelvin_values:
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")