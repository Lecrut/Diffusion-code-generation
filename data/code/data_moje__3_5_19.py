def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32.0

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    print(celsius_to_fahrenheit(0))
    print(celsius_to_fahrenheit(100))
    print(fahrenheit_to_celsius(32))
    print(fahrenheit_to_celsius(212))
    print(kelvin_to_celsius(273.15))
    print(kelvin_to_celsius(373.15))