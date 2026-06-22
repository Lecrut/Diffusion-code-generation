def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be negative")
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 500]
    for kelvin in sample_kelvin_values:
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"Kelvin: {kelvin} -> Fahrenheit: {fahrenheit}")