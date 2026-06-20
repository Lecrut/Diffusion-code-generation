def celsius_to_fahrenheit(c):
    return c * 1.8 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8

def kelvin_to_celsius(k):
    return k - 273.15

if __name__ == '__main__':
    print(celsius_to_fahrenheit(0))
    print(fahrenheit_to_celsius(32))
    print(kelvin_to_celsius(0))