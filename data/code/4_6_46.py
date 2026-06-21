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
    
    normalized_value = distance * conversion_factors[unit]
    return normalized_value

if __name__ == '__main__':
    sample_distances = [
        (2, 'yd'),
        (750, 'mm'),
        (3.5, 'mi'),
        (15, 'in'),
        (8, 'km')
    ]
    
    for distance, unit in sample_distances:
        normalized = normalize_distance(distance, unit)
        print(f"{distance} {unit} is {normalized} meters")