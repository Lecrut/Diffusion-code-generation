CONVERSION_FACTOR = 9 / 5
OFFSET = 32

def celsius_to_fahrenheit(celsius_list):
    return [(c * CONVERSION_FACTOR) + OFFSET for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, -10, 0, 25, 100]
    fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)