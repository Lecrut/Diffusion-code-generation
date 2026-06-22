def normalize_distance(distance, unit):
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
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return distance * conversion_factors[unit]

if __name__ == '__main__':
    distances = [
        (15, 'km'),
        (750, 'cm'),
        (24, 'in'),
        (6, 'yd'),
        (3.2, 'mi')
    ]
    
    for distance, unit in distances:
        normalized = normalize_distance(distance, unit)
        print(f'{distance} {unit} is {normalized} meters')