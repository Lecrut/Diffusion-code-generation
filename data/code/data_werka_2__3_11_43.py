def celsius_to_fahrenheit(celsius_list):
    conversion_table = {
        'celsius': 9/5,
        'base_temperature': 32
    }
    return [c * conversion_table['celsius'] + conversion_table['base_temperature'] for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, 0, 100, 37]
    fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)