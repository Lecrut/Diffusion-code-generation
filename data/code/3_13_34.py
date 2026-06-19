def kelvin_to_celsius(kelvin_list):
    celsius_list = []
    for temp in kelvin_list:
        if isinstance(temp, (int, float)) and temp >= 0:
            celsius_list.append(temp - 273.15)
        else:
            celsius_list.append(None)
    return celsius_list
if __name__ == '__main__':
    sample_kelvin_temps = [273.15, 0, 300, -50, 'invalid', 100]
    converted_temps = kelvin_to_celsius(sample_kelvin_temps)
    print(converted_temps)