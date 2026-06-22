def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == '__main__':
    sample_celsius = 25
    sample_fahrenheit = 70
    
    converted_fahrenheit = celsius_to_fahrenheit(sample_celsius)
    converted_celsius = fahrenheit_to_celsius(sample_fahrenheit)
    
    print(f"{sample_celsius}°C is {converted_fahrenheit}°F")
    print(f"{sample_fahrenheit}°F is {converted_celsius}°C")