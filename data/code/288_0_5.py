import sys
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)
def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
if __name__ == '__main__':
    celsius_temp = 25.0
    fahrenheit_temp = 77.0
    kelvin_temp = 298.15
    print(f"Celsius to Fahrenheit: {celsius_to_fahrenheit(celsius_temp):.2f}")
    print(f"Fahrenheit to Celsius: {fahrenheit_to_celsius(fahrenheit_temp):.2f}")
    print(f"Celsius to Kelvin: {celsius_to_kelvin(celsius_temp):.2f}")
    print(f"Kelvin to Celsius: {kelvin_to_celsius(kelvin_temp):.2f}")
    print(f"Fahrenheit to Kelvin: {fahrenheit_to_kelvin(fahrenheit_temp):.2f}")
    print(f"Kelvin to Fahrenheit: {kelvin_to_fahrenheit(kelvin_temp):.2f}")