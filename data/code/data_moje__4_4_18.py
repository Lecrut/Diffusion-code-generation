def convert_distance(distance, target_unit):
    conversion_to_meters = {'km': 1000.0, 'm': 1.0, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.344, 'ft': 0.3048, 'in': 0.0254}
    if target_unit not in conversion_to_meters:
        raise ValueError(f'Invalid unit: {target_unit}')
    factor = conversion_to_meters[target_unit]
    if factor == 0:
        raise ZeroDivisionError('Conversion factor is zero')
    converted_distance = distance / factor
    return converted_distance
if __name__ == '__main__':
    sample_distance = 1000.0
    target_units = ['km', 'm', 'cm', 'mm', 'mi', 'ft', 'in']
    for unit in target_units:
        result = convert_distance(sample_distance, unit)
        print(result)
    try:
        convert_distance(sample_distance, 'ly')
    except ValueError as e:
        print(e)
    try:
        convert_distance(sample_distance, 'invalid')
    except ValueError as e:
        print(e)