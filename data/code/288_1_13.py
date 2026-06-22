def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

if __name__ == '__main__':
    temperature = 20
    celsius = kelvin_to_celsius(temperature)
    fahrenheit = kelvin_to_fahrenheit(temperature)
    print(f"Celsius: {celsius}, Fahrenheit: {fahrenheit}")