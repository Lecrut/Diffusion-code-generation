def convert_temp(celsius_list):
    conversion_map = {'factor': 9/5, 'offset': 32}
    return [c * conversion_map['factor'] + conversion_map['offset'] for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [25, -10, 100, 30]
    fahrenheit_temps = convert_temp(sample_temps)
    print(fahrenheit_temps)