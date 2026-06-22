def normalize_distance(value, unit):
    conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return value * conversion_factors[unit]

if __name__ == '__main__':
    distances = [
        (10, 'meters'),
        (5, 'kilometers'),
        (2, 'miles')
    ]
    
    for distance, unit in distances:
        normalized_distance = normalize_distance(distance, unit)
        print(f"{distance} {unit} is {normalized_distance} meters")