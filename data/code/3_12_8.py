def convert_celsius_to_fahrenheit(celsius_values):
    return [(c * 9 / 5) + 32 for c in celsius_values]

if __name__ == '__main__':
    sample_data = [-40, 0, 25, 100, 37.5]
    result = convert_celsius_to_fahrenheit(sample_data)
    print(result)