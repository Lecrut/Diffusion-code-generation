def convert_distance(distance, target_unit):
    if distance < 0:
        raise ValueError('Distance cannot be negative')
    conversion_factors = {'m': 1.0, 'km': 0.001, 'cm': 100.0, 'mm': 1000.0, 'mi': 0.000621371, 'ft': 3.28084, 'in': 39.3701}
    if target_unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {target_unit}')
    return distance * conversion_factors[target_unit]
if __name__ == '__main__':
    try:
        distance = 150.0
        target_unit = 'km'
        converted_distance = convert_distance(distance, target_unit)
        print(converted_distance)
    except ValueError as e:
        print(e)