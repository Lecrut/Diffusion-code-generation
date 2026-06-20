def normalize_to_meters(distance, unit):
    unit = unit.lower()
    conversion_factors = {'m': 1.0, 'km': 1000.0, 'cm': 0.01, 'mm': 0.001, 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.34}
    if unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    return distance * conversion_factors[unit]
if __name__ == '__main__':
    sample_distances = [(1000, 'm'), (5, 'km'), (250, 'cm'), (100, 'mm'), (49.21, 'in'), (3.28, 'ft'), (1.09, 'yd'), (0.62, 'mi')]
    for distance, unit in sample_distances:
        normalized_distance = normalize_to_meters(distance, unit)
        print(f'{distance} {unit} = {normalized_distance} m')