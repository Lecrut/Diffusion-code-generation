def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
if __name__ == '__main__':
    sample_celsius = 25
    sample_fahrenheit = 77
    sample_kelvin = 300
    converted_fahrenheit = celsius_to_fahrenheit(sample_celsius)
    print(f'Celsius {sample_celsius} to Fahrenheit: {converted_fahrenheit}')
    converted_celsius = fahrenheit_to_celsius(sample_fahrenheit)
    print(f'Fahrenheit {sample_fahrenheit} to Celsius: {converted_celsius}')
    converted_celsius_from_kelvin = kelvin_to_celsius(sample_kelvin)
    print(f'Kelvin {sample_kelvin} to Celsius: {converted_celsius_from_kelvin}')