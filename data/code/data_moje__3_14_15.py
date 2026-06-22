def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0 + 273.15

if __name__ == '__main__':
    print(fahrenheit_to_kelvin(32.0))
    print(fahrenheit_to_kelvin(212.0))
    print(fahrenheit_to_kelvin(98.6))