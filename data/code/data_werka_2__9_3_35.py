def convert_to_liters(volume, unit):
    conversion_factors = {
        'ml': 1e-3,
        'cl': 1e-2,
        'dl': 1e-1,
        'l': 1.0,
        'hl': 100.0,
        'm3': 1000.0,
        'gal': 3.785411784,
        'qt': 0.946352946,
        'pt': 0.473176473,
        'fl oz': 2.957352956e-2
    }
    
    if unit.lower() not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return volume * conversion_factors[unit.lower()]

if __name__ == '__main__':
    sample_values = [
        (100, 'ml'),
        (50, 'cl'),
        (2, 'dl'),
        (1, 'l'),
        (0.5, 'hl'),
        (0.001, 'm3'),
        (1, 'gal'),
        (4, 'qt'),
        (8, 'pt'),
        (32, 'fl oz')
    ]
    
    for volume, unit in sample_values:
        print(f"{volume} {unit} is {convert_to_liters(volume, unit)} liters")