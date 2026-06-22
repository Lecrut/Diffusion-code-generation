def convert_distance(distance, target_unit):
    conversion_factors = {'meters': 1.0, 'kilometers': 0.001, 'centimeters': 100.0, 'millimeters': 1000.0, 'miles': 0.000621371, 'yards': 1.09361, 'feet': 3.28084, 'inches': 39.3701}
    if target_unit not in conversion_factors:
        raise ValueError(f'Unsupported target unit: {target_unit}')
    converted_distance = distance * conversion_factors[target_unit]
    return converted_distance
if __name__ == '__main__':
    sample_distance = 100.0
    target_units = ['kilometers', 'feet', 'inches']
    for unit in target_units:
        try:
            result = convert_distance(sample_distance, unit)
            print(f'{sample_distance} meters is {result:.6f} {unit}')
        except ValueError as e:
            print(e)