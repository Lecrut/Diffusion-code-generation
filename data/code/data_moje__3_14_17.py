def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9

if __name__ == '__main__':
    sample_values = [32, 212, -459.67, 0, 100]
    for value in sample_values:
        print(fahrenheit_to_kelvin(value))