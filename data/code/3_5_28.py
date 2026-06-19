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
    
    print(f"Celsius to Fahrenheit: {sample_celsius}C -> {celsius_to_fahrenheit(sample_celsius)}F")
    print(f"Fahrenheit to Celsius: {sample_fahrenheit}F -> {fahrenheit_to_celsius(sample_fahrenheit)}C")
    print(f"Kelvin to Celsius: {sample_kelvin}K -> {kelvin_to_celsius(sample_kelvin)}C")