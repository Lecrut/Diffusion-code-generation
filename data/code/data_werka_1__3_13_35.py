def kelvin_to_celsius(kelvin_list):
    return [k - 273.15 for k in kelvin_list if isinstance(k, (int, float))]
if __name__ == '__main__':
    sample_temperatures = [0, 273.15, 300, 500, -100]
    converted_temperatures = kelvin_to_celsius(sample_temperatures)
    print(converted_temperatures)