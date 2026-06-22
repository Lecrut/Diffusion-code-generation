def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperature must be a number")
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Temperature must be a number")
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    if not isinstance(kelvin, (int, float)) or kelvin < 0:
        raise ValueError("Kelvin temperature cannot be below absolute zero")
    return kelvin - 273.15

if __name__ == '__main__':
    sample_celsius = 37
    sample_fahrenheit = 98.6
    sample_kelvin = 310.93
    print(f"{sample_celsius}C is {celsius_to_fahrenheit(sample_celsius)}F")
    print(f"{sample_fahrenheit}F is {fahrenheit_to_celsius(sample_fahrenheit)}C")
    print(f"{sample_kelvin}K is {kelvin_to_celsius(sample_kelvin)}C")