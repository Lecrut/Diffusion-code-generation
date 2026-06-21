def convert_to_meters(distance, unit):
    conversion_factors = {
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }
    return conversion_factors.get(unit, None)

def normalize_distance(distance, unit):
    factor = convert_to_meters(1, unit)
    if factor is None:
        raise ValueError(f"Unsupported unit: {unit}")
    return distance * factor

if __name__ == '__main__':
    sample_values = [
        (10, 'km'),
        (500, 'm'),
        (12, 'in'),
        (3, 'yd'),
        (2.5, 'mi')
    ]
    for value, unit in sample_values:
        normalized = normalize_distance(value, unit)
        print(f'{value} {unit} is {normalized} meters')