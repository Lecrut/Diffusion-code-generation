def convert_to_liters(volume, unit):
    conversion_factors = {
        'm3': 1000,
        'cm3': 0.001,
        'mm3': 0.000001,
        'dm3': 1,
        'in3': 0.016387064,
        'ft3': 28.316846592,
        'gal': 3.785411784,
        'qt': 0.946352946,
        'pt': 0.473176473,
        'fl oz': 0.02957352956
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return volume * conversion_factors[unit]

if __name__ == '__main__':
    sample_volumes = [
        (1, 'm3'),
        (1000, 'cm3'),
        (1000000, 'mm3'),
        (1, 'dm3'),
        (1, 'in3'),
        (1, 'ft3'),
        (1, 'gal'),
        (1, 'qt'),
        (1, 'pt'),
        (1, 'fl oz')
    ]
    
    for volume, unit in sample_volumes:
        print(f"{volume} {unit} is {convert_to_liters(volume, unit)} liters")