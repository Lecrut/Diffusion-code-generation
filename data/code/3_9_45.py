def kelvin_to_celsius(kelvin_list):
    def is_valid_temperature(temp):
        return isinstance(temp, (int, float)) and temp >= 0

    celsius_list = []
    for temp in kelvin_list:
        if is_valid_temperature(temp):
            celsius_temp = temp - 273.15
            celsius_list.append(celsius_temp)
        else:
            celsius_list.append(None)
    return celsius_list

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 400, -10, 'abc', None]
    converted_celsius_values = kelvin_to_celsius(sample_kelvin_values)
    print(converted_celsius_values)