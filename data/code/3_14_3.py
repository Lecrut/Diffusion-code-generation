def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    test_values = [32, 212, -40, 98.6, 0]
    for value in test_values:
        result = fahrenheit_to_kelvin(value)
        print(f"{value} F is {result} K")