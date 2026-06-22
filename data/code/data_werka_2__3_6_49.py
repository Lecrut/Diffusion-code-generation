def convert_temp(celsius_list):
    CONVERSION_FACTOR = 9 / 5
    BASE_OFFSET = 32
    return [c * CONVERSION_FACTOR + BASE_OFFSET for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [-40, 0, 100, 37]
    fahrenheit_temps = convert_temp(sample_temps)
    print(fahrenheit_temps)