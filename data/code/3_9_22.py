def convert_temp(celsius_list):
    return [c * 9/5 + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temps_celsius = [0, 10, 20, 30, 40]
    converted_temps_fahrenheit = convert_temp(sample_temps_celsius)
    print(converted_temps_fahrenheit)