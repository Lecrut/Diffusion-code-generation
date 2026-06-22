def celsius_to_fahrenheit(celsius_list):
    conversion_table = {
        'factor': 9 / 5,
        'offset': 32
    }
    return [(c * conversion_table['factor']) + conversion_table['offset'] for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, -18, 0, 37, 100]
    fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)