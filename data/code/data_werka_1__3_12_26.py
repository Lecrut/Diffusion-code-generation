def celsius_to_fahrenheit(celsius_values):
    return [(c * 9/5) + 32 for c in celsius_values]

if __name__ == '__main__':
    sample_celsius = [0, 10, 20, 30, 40, 50]
    converted_fahrenheit = celsius_to_fahrenheit(sample_celsius)
    print(converted_fahrenheit)