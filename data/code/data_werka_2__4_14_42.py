def normalize_distance(distance, unit):
    conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return distance * conversion_factors[unit]

if __name__ == '__main__':
    sample_values = [
        (10, 'meters'),
        (5, 'kilometers'),
        (2, 'miles')
    ]
    
    for distance, unit in sample_values:
        normalized_distance = normalize_distance(distance, unit)
        print(f"{distance} {unit} is {normalized_distance} meters")