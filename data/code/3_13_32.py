def kelvin_to_celsius(kelvin_list):
    return [(k - 273.15) for k in kelvin_list if isinstance(k, (int, float))]

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 459.67, -100, 'abc', None]
    converted_celsius_values = kelvin_to_celsius(sample_kelvin_values)
    print(converted_celsius_values)