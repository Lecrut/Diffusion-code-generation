def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def kelvin_to_rankine(kelvin):
    return kelvin * 9/5

if __name__ == '__main__':
    temperature_kelvin = 300
    print(f"Celsius: {kelvin_to_celsius(temperature_kelvin)}")
    print(f"Fahrenheit: {kelvin_to_fahrenheit(temperature_kelvin)}")
    print(f"Rankine: {kelvin_to_rankine(temperature_kelvin)}")