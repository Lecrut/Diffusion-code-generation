def celsius_to_fahrenheit(celsius_values):
    return [(c * 9 / 5) + 32 for c in celsius_values]

if __name__ == '__main__':
    sample_temperatures = [-40, 0, 25, 37, 100]
    fahrenheit_results = celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_results)