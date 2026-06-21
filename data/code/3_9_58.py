def kelvin_to_celsius(kelvin_list):
    celsius_list = []
    for temp in kelvin_list:
        if isinstance(temp, (int, float)) and temp >= 0:
            converted_temp = temp - 273.15
            celsius_list.append(converted_temp)
        else:
            celsius_list.append(None)
    return celsius_list

if __name__ == '__main__':
    sample_kelvin_temps = [0, 273.15, 300, 400, -10, 'xyz', None]
    converted_celsius_temps = kelvin_to_celsius(sample_kelvin_temps)
    print(converted_celsius_temps)