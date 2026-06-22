def convert_to_liters(volume, unit):
    conversion_factors = {
        'm3': 1000,
        'cm3': 0.001,
        'mm3': 0.000001,
        'dm3': 1,
        'L': 1,
        'dL': 0.1,
        'cL': 0.01,
        'mL': 0.001,
        'gal': 3.785411784,
        'qt': 0.946352946,
        'pt': 0.473176473,
        'fl oz': 0.02957352956,
        'tsp': 0.00492892159,
        'Tbsp': 0.01478676478
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return volume * conversion_factors[unit]

if __name__ == '__main__':
    sample_values = [
        (2, 'm3'),
        (500, 'cm3'),
        (1000000, 'mm3'),
        (1.5, 'dm3'),
        (0.75, 'L'),
        (50, 'dL'),
        (250, 'cL'),
        (100, 'mL'),
        (1, 'gal'),
        (4, 'qt'),
        (8, 'pt'),
        (32, 'fl oz'),
        (64, 'tsp'),
        (2, 'Tbsp')
    ]
    
    for volume, unit in sample_values:
        print(f"{volume} {unit} is {convert_to_liters(volume, unit)} L")