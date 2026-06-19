def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == '__main__':
    sample_celsius = 25
    sample_fahrenheit = 77
    sample_kelvin = 298.15
    
    print("Celsius to Fahrenheit:", celsius_to_fahrenheit(sample_celsius))
    print("Fahrenheit to Celsius:", fahrenheit_to_celsius(sample_fahrenheit))
    print("Kelvin to Celsius:", kelvin_to_celsius(sample_kelvin))