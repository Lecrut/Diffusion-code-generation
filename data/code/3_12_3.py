def celsius_to_fahrenheit(celsius_list):
    return [((c * 9 / 5) + 32) for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, -10, 0, 25, 37, 100]
    fahrenheit_values = celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_values)