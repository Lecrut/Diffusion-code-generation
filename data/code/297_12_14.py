def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

if __name__ == '__main__':
    sample_fahrenheit = 100.0
    sample_celsius = -40.0
    
    converted_celsius = fahrenheit_to_celsius(sample_fahrenheit)
    converted_fahrenheit = celsius_to_fahrenheit(sample_celsius)
    
    print(f"{sample_fahrenheit}F is {converted_celsius:.2f}C")
    print(f"{sample_celsius}C is {converted_fahrenheit:.2f}F")