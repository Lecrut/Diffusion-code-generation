def normalize_distance(distance, unit):
    conversion_factors = {'m': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001, 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.34}
    if unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    normalized_distance = distance * conversion_factors[unit]
    return normalized_distance
if __name__ == '__main__':
    distances = [(10, 'km'), (500, 'm'), (12, 'in'), (3, 'yd'), (2.5, 'mi')]
    for distance, unit in distances:
        normalized = normalize_distance(distance, unit)
        print(f'{distance} {unit} is {normalized} meters')