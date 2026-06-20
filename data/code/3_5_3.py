def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    celsius_val = 100
    fahrenheit_val = 212
    kelvin_val = 373.15

    print(celsius_to_fahrenheit(celsius_val))
    print(fahrenheit_to_celsius(fahrenheit_val))
    print(kelvin_to_celsius(kelvin_val))