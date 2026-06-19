def normalize_distance(value, unit):
    conversion_factors = {'m': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254}
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        raise ValueError('Unsupported unit')
if __name__ == '__main__':
    distance_values = [(10, 'km'), (25.4, 'cm'), (100, 'm'), (39.37, 'in'), (1, 'mi')]
    for value, unit in distance_values:
        normalized_value = normalize_distance(value, unit)
        print(f'{value} {unit} is {normalized_value} meters')