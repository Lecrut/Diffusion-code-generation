def kelvin_to_celsius(kelvin_temps):
    return [(temp - 273.15) for temp in kelvin_temps if isinstance(temp, (int, float))]

if __name__ == '__main__':
    sample_temps = [0, 273.15, 373.15, 'abc', None, 400]
    converted_temps = kelvin_to_celsius(sample_temps)
    print(converted_temps)