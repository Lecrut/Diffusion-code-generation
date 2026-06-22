def convert_distance(distance, target_unit):
    conversion_factors = {'m': 1.0, 'km': 0.001, 'cm': 100.0, 'mm': 1000.0, 'mi': 0.000621371, 'ft': 3.28084, 'in': 39.3701}
    if distance == 0:
        return 0
    if target_unit not in conversion_factors:
        raise ValueError('Invalid target unit')
    converted_distance = distance * conversion_factors[target_unit]
    return converted_distance
if __name__ == '__main__':
    sample_distance = 100.0
    target_units = ['km', 'cm', 'mi', 'ft', 'in']
    for unit in target_units:
        result = convert_distance(sample_distance, unit)
        print(f'{sample_distance} meters is {result:.4f} {unit}')