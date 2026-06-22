def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == '__main__':
    sample_celsius = 25
    sample_fahrenheit = 77
    
    print(f"Celsius {sample_celsius} to Fahrenheit: {celsius_to_fahrenheit(sample_celsius)}")
    print(f"Fahrenheit {sample_fahrenheit} to Celsius: {fahrenheit_to_celsius(sample_fahrenheit)}")