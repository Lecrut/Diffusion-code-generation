def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    sample_values = [32.0, 212.0, -40.0, 98.6]
    for value in sample_values:
        print(fahrenheit_to_kelvin(value))