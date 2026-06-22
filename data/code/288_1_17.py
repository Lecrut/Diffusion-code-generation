def kelvin_to_celsius(temp):
    return temp - 273.15

def kelvin_to_fahrenheit(temp):
    return (temp - 273.15) * 9 / 5 + 32

def convert_temp(temp, source_scale):
    if source_scale == 'Kelvin':
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        return {'Celsius': celsius, 'Fahrenheit': fahrenheit}
    else:
        raise ValueError('Unsupported source scale')
if __name__ == '__main__':
    test_cases = [(273.15, 'Kelvin'), (373.15, 'Kelvin'), (0, 'Kelvin')]
    for temp, scale in test_cases:
        try:
            result = convert_temp(temp, scale)
            print(f'{temp} {scale} is {result['Celsius']} Celsius and {result['Fahrenheit']} Fahrenheit')
        except ValueError as e:
            print(e)