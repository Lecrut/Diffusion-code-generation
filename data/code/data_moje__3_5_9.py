def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    print(celsius_to_fahrenheit(0))
    print(fahrenheit_to_celsius(32))
    print(kelvin_to_celsius(273.15))