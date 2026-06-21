def convert_temp(celsius_list):
    conversion_table = {
        'factor': 9/5,
        'offset': 32
    }
    return [c * conversion_table['factor'] + conversion_table['offset'] for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [-40, 0, 100, 37]
    fahrenheit_temps = convert_temp(sample_temps)
    print(fahrenheit_temps)