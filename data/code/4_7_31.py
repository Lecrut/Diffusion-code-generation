def normalize_distance(value, unit):
    conversion_factors = {'m': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254}
    if unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    normalized_value = value * conversion_factors[unit]
    return normalized_value
if __name__ == '__main__':
    sample_values = [(10, 'km'), (250, 'cm'), (5.5, 'yd'), (100, 'in')]
    for value, unit in sample_values:
        normalized_value = normalize_distance(value, unit)
        print(f'{value} {unit} is {normalized_value} meters')