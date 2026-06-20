def kelvin_to_celsius(kelvin_list):
    celsius_list = []
    for temp in kelvin_list:
        if not isinstance(temp, (int, float)):
            continue
        if temp < 0:
            celsius_list.append(None)
        else:
            celsius_list.append(temp - 273.15)
    return celsius_list

if __name__ == '__main__':
    sample_kelvins = [300, 0, -10, 273.15, 100, "invalid", None]
    result = kelvin_to_celsius(sample_kelvins)
    print(result)