def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0 + 273.15

if __name__ == '__main__':
    sample_values = [32, 212, -459.67]
    for value in sample_values:
        print(fahrenheit_to_kelvin(value))