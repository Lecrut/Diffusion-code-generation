def convert_to_meters(distance, unit):
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
    
    meters = distance * conversion_factors[unit]
    return meters

if __name__ == '__main__':
    sample_values = [
        (2.5, 'yd'),
        (1000, 'mm'),
        (3.4, 'ft'),
        (0.5, 'km'),
        (78, 'in')
    ]
    
    for distance, unit in sample_values:
        normalized_distance = convert_to_meters(distance, unit)
        print(f'{distance} {unit} is {normalized_distance} meters')