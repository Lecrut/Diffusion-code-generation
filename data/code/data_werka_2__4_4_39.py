def convert_distance(distance, target_unit):
    conversion_factors = {'meters_to_kilometers': 1 / 1000, 'kilometers_to_meters': 1000, 'meters_to_feet': 3.28084, 'feet_to_meters': 1 / 3.28084, 'kilometers_to_miles': 0.621371, 'miles_to_kilometers': 1 / 0.621371}
    if distance == 0:
        raise ValueError('Distance cannot be zero.')
    if target_unit not in conversion_factors:
        raise ValueError(f'Unsupported target unit: {target_unit}')
    converted_distance = distance * conversion_factors[target_unit]
    return converted_distance
if __name__ == '__main__':
    try:
        distance = 1000
        target_unit = 'kilometers_to_miles'
        result = convert_distance(distance, target_unit)
        print(result)
    except ValueError as e:
        print(e)