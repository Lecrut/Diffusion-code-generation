def normalize_distance(value, unit):
    METER_TO_KILOMETER = 0.001
    METER_TO_MILE = 0.000621371

    conversion_factors = {
        'meters': 1,
        'kilometers': 1 / METER_TO_KILOMETER,
        'miles': 1 / METER_TO_MILE
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return value * conversion_factors[unit]

if __name__ == '__main__':
    sample_values = [
        (10, 'meters'),
        (5, 'kilometers'),
        (2, 'miles')
    ]
    for distance, unit in sample_values:
        normalized_distance = normalize_distance(distance, unit)
        print(f"{distance} {unit} is {normalized_distance:.4f} meters")