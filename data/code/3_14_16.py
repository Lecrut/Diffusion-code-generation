def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    test_values = [32, 212, -40, 98.6]
    for value in test_values:
        print(fahrenheit_to_kelvin(value))