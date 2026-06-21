def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin temperature cannot be below absolute zero")
    return kelvin - 273.15

if __name__ == '__main__':
    sample_celsius = 30
    sample_fahrenheit = 86
    sample_kelvin = 303.15
    
    converted_to_fahrenheit = celsius_to_fahrenheit(sample_celsius)
    converted_to_celsius = fahrenheit_to_celsius(sample_fahrenheit)
    converted_from_kelvin = kelvin_to_celsius(sample_kelvin)
    
    print(f"{sample_celsius}C is {converted_to_fahrenheit}F")
    print(f"{sample_fahrenheit}F is {converted_to_celsius}C")
    print(f"{sample_kelvin}K is {converted_from_kelvin}C")