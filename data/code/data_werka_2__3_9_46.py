def kelvin_to_celsius(kelvin_list):
    conversion_map = {
        'kelvin': 273.15,
        'celsius': 0
    }
    celsius_list = []
    for temp in kelvin_list:
        if isinstance(temp, (int, float)) and temp >= conversion_map['kelvin']:
            celsius_temp = temp - conversion_map['kelvin']
            celsius_list.append(celsius_temp)
        else:
            celsius_list.append(None)
    return celsius_list

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 400, -100, 'abc', None]
    converted_values = kelvin_to_celsius(sample_kelvin_values)
    print(converted_values)