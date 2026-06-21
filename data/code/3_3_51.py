def validate_temperature(temp, scale):
    if temp < 0 and scale == 'Kelvin':
        raise ValueError("Kelvin temperature cannot be below absolute zero")

def celsius_to_fahrenheit(celsius):
    validate_temperature(celsius, 'Celsius')
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    validate_temperature(fahrenheit, 'Fahrenheit')
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    validate_temperature(kelvin, 'Kelvin')
    return kelvin - 273.15

if __name__ == '__main__':
    sample_celsius = 150
    sample_fahrenheit = 302
    sample_kelvin = 423.15
    print(f"{sample_celsius}C is {celsius_to_fahrenheit(sample_celsius)}F")
    print(f"{sample_fahrenheit}F is {fahrenheit_to_celsius(sample_fahrenheit)}C")
    print(f"{sample_kelvin}K is {kelvin_to_celsius(sample_kelvin)}C")