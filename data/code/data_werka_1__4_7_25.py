def normalize_distance(distance, unit):
    conversion_factors = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.34,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return distance * conversion_factors[unit]

if __name__ == '__main__':
    sample_distances = [
        (10, 'km'),
        (100, 'cm'),
        (500, 'mm'),
        (2, 'mi'),
        (100, 'yd'),
        (36, 'ft'),
        (12, 'in')
    ]
    
    for distance, unit in sample_distances:
        normalized_distance = normalize_distance(distance, unit)
        print(f"{distance} {unit} is {normalized_distance} meters")