def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0 + 273.15

if __name__ == '__main__':
    sample_fahrenheit_values = [32.0, 212.0, -459.67, 68.0, 98.6]
    for f in sample_fahrenheit_values:
        k = fahrenheit_to_kelvin(f)
        print(k)