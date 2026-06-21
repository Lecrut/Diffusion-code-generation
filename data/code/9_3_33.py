def convert_to_liters(volume, unit):
    conversion_factors = {
        'ml': 1e-3,
        'cl': 1e-2,
        'dl': 1e-1,
        'l': 1.0,
        'fl oz': 0.0295735296,
        'cup': 0.2365882365,
        'pt': 0.473176473,
        'qt': 0.946352946,
        'gal': 3.785411784
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
        (8, 'fl oz'),
        (2, 'cup'),
        (1, 'pt'),
        (1, 'qt'),
        (1, 'gal')
    ]
    
    for volume, unit in sample_values:
        print(f"{volume} {unit} is {convert_to_liters(volume, unit)} liters")