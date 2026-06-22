def convert_distance(distance, target_unit):
    conversion_factors = {'meters': 1.0, 'kilometers': 0.001, 'centimeters': 100.0, 'millimeters': 1000.0, 'inches': 39.3701, 'feet': 3.28084, 'yards': 1.09361, 'miles': 0.000621371}
    if target_unit not in conversion_factors:
        raise ValueError(f'Invalid target unit: {target_unit}')
    try:
        converted_distance = distance / conversion_factors['meters'] * conversion_factors[target_unit]
    except ZeroDivisionError:
        return 0.0
    return converted_distance
if __name__ == '__main__':
    sample_distance = 150.0
    target_unit = 'feet'
    result = convert_distance(sample_distance, target_unit)
    print(result)