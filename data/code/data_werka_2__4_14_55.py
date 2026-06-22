def normalize_distance(value, unit):
    METER_CONVERSIONS = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34
    }
    
    if unit not in METER_CONVERSIONS:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return value * METER_CONVERSIONS[unit]

if __name__ == '__main__':
    sample_values = [
        (15, 'meters'),
        (3, 'kilometers'),
        (1, 'miles')
    ]
    for distance, unit in sample_values:
        normalized_distance = normalize_distance(distance, unit)
        print(f"{distance} {unit} is {normalized_distance} meters")