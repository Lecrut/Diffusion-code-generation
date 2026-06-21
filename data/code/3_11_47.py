def celsius_to_fahrenheit(celsius_list):
    conversion_table = {
        'factor': 9/5,
        'base': 32
    }
    return [c * conversion_table['factor'] + conversion_table['base'] for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [30, -10, 100, 25]
    fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)