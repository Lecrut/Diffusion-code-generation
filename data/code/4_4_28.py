def convert_distance(distance, target_unit):
    conversion_factors = {'meters': 1.0, 'kilometers': 0.001, 'centimeters': 100.0, 'millimeters': 1000.0, 'inches': 39.37008, 'feet': 3.28084, 'yards': 1.09361, 'miles': 0.000621371}
    if distance == 0:
        return 0
    if target_unit not in conversion_factors:
        raise ValueError(f'Unsupported target unit: {target_unit}')
    converted_distance = distance * conversion_factors[target_unit]
    return converted_distance
if __name__ == '__main__':
    distance_in_meters = 100.0
    target_unit = 'kilometers'
    converted_value = convert_distance(distance_in_meters, target_unit)
    print(converted_value)