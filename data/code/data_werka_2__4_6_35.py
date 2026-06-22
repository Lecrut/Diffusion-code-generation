def validate_unit(unit):
    supported_units = {'m', 'km', 'cm', 'mm', 'in', 'ft', 'yd', 'mi'}
    if unit not in supported_units:
        raise ValueError(f'Unsupported unit: {unit}')

def normalize_distance(distance, unit):
    validate_unit(unit)
    conversion_factors = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }
    return distance * conversion_factors[unit]

if __name__ == '__main__':
    sample_values = [
        (2, 'm'),
        (5, 'km'),
        (100, 'cm'),
        (250, 'mm'),
        (12, 'in'),
        (6, 'ft'),
        (1, 'yd'),
        (0.5, 'mi')
    ]
    for distance, unit in sample_values:
        normalized = normalize_distance(distance, unit)
        print(f'{distance} {unit} is {normalized} meters')