def convert_volume_to_liters(volume, unit):
    conversion_factors = {
        'ml': 0.001,
        'cl': 0.01,
        'dl': 0.1,
        'l': 1.0,
        'fl oz': 0.0295735,
        'cup': 0.236588,
        'pt': 0.473176,
        'qt': 0.946353,
        'gal': 3.78541,
    }
    
    if unit.lower() not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return volume * conversion_factors[unit.lower()]

if __name__ == '__main__':
    sample_values = [
        (100, 'ml'),
        (2, 'cl'),
        (5, 'dl'),
        (3.5, 'l'),
        (8, 'fl oz'),
        (4, 'cup'),
        (2, 'pt'),
        (1, 'qt'),
        (0.25, 'gal')
    ]
    
    for volume, unit in sample_values:
        print(f"{volume} {unit} is {convert_volume_to_liters(volume, unit)} liters")