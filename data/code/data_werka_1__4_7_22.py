def normalize_distance(value, unit):
    conversion_factors = {'m': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001, 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.34}
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        raise ValueError('Unsupported unit')
if __name__ == '__main__':
    distances = [(10, 'km'), (250, 'cm'), (3.5, 'ft'), (1, 'mi')]
    for value, unit in distances:
        normalized_value = normalize_distance(value, unit)
        print(f'{value} {unit} is {normalized_value} meters')