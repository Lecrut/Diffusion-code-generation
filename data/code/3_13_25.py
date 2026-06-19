def kelvin_to_celsius(kelvin_list):
    return [(k - 273.15) for k in kelvin_list]

if __name__ == '__main__':
    sample_kelvin_values = [0, 273.15, 300, 400, 500]
    converted_celsius_values = kelvin_to_celsius(sample_kelvin_values)
    print(converted_celsius_values)