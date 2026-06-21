def convert_temp(celsius_list):
    conversion_factor = 9 / 5
    base_offset = 32
    return [c * conversion_factor + base_offset for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [10, -40, 100, 0]
    fahrenheit_temps = convert_temp(sample_temps)
    print(fahrenheit_temps)