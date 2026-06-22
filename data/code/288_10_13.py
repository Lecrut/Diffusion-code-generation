def celsius_to_fahrenheit(celsius):
    return (celsius * 9 // 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 // 9

if __name__ == '__main__':
    sample_celsius = 10
    sample_fahrenheit = 50
    
    print(f"Celsius {sample_celsius} is Fahrenheit {celsius_to_fahrenheit(sample_celsius)}")
    print(f"Fahrenheit {sample_fahrenheit} is Celsius {fahrenheit_to_celsius(sample_fahrenheit)}")