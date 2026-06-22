def convert_temp(celsius_list):
    return [(c * 9/5) + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_celsius = [-40, 0, 10, 25, 37, 100]
    sample_fahrenheit = convert_temp(sample_celsius)
    print(sample_fahrenheit)