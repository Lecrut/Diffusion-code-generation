def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def kelvin_to_rankine(kelvin):
    return kelvin * 9/5

if __name__ == '__main__':
    sample_kelvin = 300
    print(f"Celsius: {kelvin_to_celsius(sample_kelvin):.2f}°C")
    print(f"Fahrenheit: {kelvin_to_fahrenheit(sample_kelvin):.2f}°F")
    print(f"Rankine: {kelvin_to_rankine(sample_kelvin):.2f}°R")