def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

if __name__ == '__main__':
    samples = [32, 212, -459.67, 0, 100]
    for sample in samples:
        print(fahrenheit_to_kelvin(sample))