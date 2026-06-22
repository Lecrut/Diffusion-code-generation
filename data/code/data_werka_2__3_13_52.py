def convert_to_celsius(fahrenheit):
    conversion_table = {
        'factor': 5 / 9,
        'offset': 32
    }
    return tuple(map(lambda f: (f - conversion_table['offset']) * conversion_table['factor'], fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (45, 86, 130, 230)
    celsius_temperatures = convert_to_celsius(sample_temperatures)
    print(celsius_temperatures)