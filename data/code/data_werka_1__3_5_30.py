def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    sample_celsius = 25
    sample_fahrenheit = 77
    sample_kelvin = 300
    
    print(f"{sample_celsius}C is {celsius_to_fahrenheit(sample_celsius)}F")
    print(f"{sample_fahrenheit}F is {fahrenheit_to_celsius(sample_fahrenheit)}C")
    print(f"{sample_kelvin}K is {kelvin_to_celsius(sample_kelvin)}C")