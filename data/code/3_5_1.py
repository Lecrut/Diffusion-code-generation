def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    c = 100
    f = 212
    k = 373.15
    
    print(celsius_to_fahrenheit(c))
    print(fahrenheit_to_celsius(f))
    print(kelvin_to_celsius(k))