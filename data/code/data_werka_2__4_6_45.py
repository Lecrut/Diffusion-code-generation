def normalize_distance(distance, unit):
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
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return distance * conversion_factors[unit]

if __name__ == '__main__':
    sample_distances = [
        (10, 'm'),
        (250, 'cm'),
        (5000, 'mm'),
        (3, 'km'),
        (12, 'in'),
        (4, 'ft'),
        (100, 'yd'),
        (5, 'mi')
    ]
    
    for distance, unit in sample_distances:
        normalized_distance = normalize_distance(distance, unit)
        print(f"{distance} {unit} is {normalized_distance} meters")