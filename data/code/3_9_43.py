def kelvin_to_celsius(kelvin_list):
    celsius_list = []
    for temp in kelvin_list:
        if isinstance(temp, (int, float)) and temp >= 0:
            celsius_list.append(temp - 273.15)
        else:
            celsius_list.append(None)
    return celsius_list
if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, -5, 'abc', None]
    converted_values = kelvin_to_celsius(sample_kelvin_values)
    print(converted_values)