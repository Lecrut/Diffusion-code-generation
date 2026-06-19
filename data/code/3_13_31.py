def kelvin_to_celsius(kelvin_list):
    return [(k - 273.15) for k in kelvin_list if isinstance(k, (int, float))]

if __name__ == '__main__':
    sample_values = [0, 273.15, 300, 500, 'invalid', None, 100]
    converted_values = kelvin_to_celsius(sample_values)
    print(converted_values)