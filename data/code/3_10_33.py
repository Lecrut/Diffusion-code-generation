def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    sample_values = [32, 212, -40, 100]
    for value in sample_values:
        print(fahrenheit_to_kelvin(value))