def celsius_to_fahrenheit(celsius_values):
    return [(c * 9 / 5) + 32 for c in celsius_values]

if __name__ == '__main__':
    sample_celsius = [0, 25, 37, 100, -40]
    print(celsius_to_fahrenheit(sample_celsius))