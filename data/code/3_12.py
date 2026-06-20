def convert_celsius_to_fahrenheit(celsius_values):
    return [(c * 9 / 5) + 32 for c in celsius_values]

if __name__ == '__main__':
    sample_temperatures = [0, 10, 25, 100, -40, 37]
    result = convert_celsius_to_fahrenheit(sample_temperatures)
    print(result)