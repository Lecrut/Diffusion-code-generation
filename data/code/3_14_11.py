def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return (fahrenheit - 32.0) * 5.0 / 9.0 + 273.15

if __name__ == '__main__':
    sample_values = [-459.67, 0, 32, 212, 1000]
    for value in sample_values:
        print(fahrenheit_to_kelvin(value))