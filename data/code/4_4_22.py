def convert_distance(distance, target_unit):
    conversion_factors = {'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000, 'inches': 39.37008, 'feet': 3.28084, 'yards': 1.09361, 'miles': 0.000621371}
    if target_unit not in conversion_factors:
        raise ValueError('Invalid target unit')
    if distance == 0 and conversion_factors[target_unit] == 0:
        return 0
    converted_distance = distance * conversion_factors[target_unit]
    return converted_distance
if __name__ == '__main__':
    sample_distance = 150.0
    target_unit = 'kilometers'
    result = convert_distance(sample_distance, target_unit)
    print(result)