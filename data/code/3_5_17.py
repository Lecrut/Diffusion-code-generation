def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    sample_celsius = 100.0
    sample_fahrenheit = 212.0
    sample_kelvin = 373.15

    print(celsius_to_fahrenheit(sample_celsius))
    print(fahrenheit_to_celsius(sample_fahrenheit))
    print(kelvin_to_celsius(sample_kelvin))