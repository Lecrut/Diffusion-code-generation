def convert_distance(distance, target_unit):
    conversion_factors = {'m': 1.0, 'km': 0.001, 'cm': 100.0, 'mm': 1000.0, 'mi': 0.000621371, 'ft': 3.28084, 'in': 39.3701}
    if target_unit not in conversion_factors:
        raise ValueError(f'Unsupported target unit: {target_unit}')
    if distance == 0:
        return 0.0
    converted_distance = distance * conversion_factors[target_unit]
    return converted_distance
if __name__ == '__main__':
    distance_in_meters = 150.0
    target_unit = 'km'
    try:
        result = convert_distance(distance_in_meters, target_unit)
        print(result)
    except ValueError as e:
        print(e)