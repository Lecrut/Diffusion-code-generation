KELVIN_ZERO = 0
CELSIUS_TO_FAHRENHEIT_MULTIPLIER = 9/5
CELSIUS_TO_FAHRENHEIT_ADDEND = 32

def kelvin_to_celsius(kelvin):
    if kelvin < KELVIN_ZERO:
        raise ValueError("Kelvin temperature cannot be negative")
    return kelvin - KELVIN_ZERO

def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_MULTIPLIER) + CELSIUS_TO_FAHRENHEIT_ADDEND

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    for kelvin in sample_kelvin_values:
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")