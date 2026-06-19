def convert_to_liters(volume, unit):
    conversion_factors = {
        'ml': 0.001,
        'cl': 0.01,
        'dl': 0.1,
        'l': 1.0,
        'fl oz': 0.0295735296,
        'cup': 0.2365882365,
        'pt': 0.473176473,
        'qt': 0.946352946,
        'gal': 3.785411784
    }
    
    if unit.lower() not in conversion_factors:
        raise ValueError("Unsupported unit")
    
    return volume * conversion_factors[unit.lower()]

if __name__ == '__main__':
    sample_volumes = [
        (100, 'ml'),
        (250, 'cl'),
        (1.5, 'dl'),
        (3, 'l'),
        (8, 'fl oz'),
        (2, 'cup'),
        (1, 'pt'),
        (0.5, 'qt'),
        (10, 'gal')
    ]
    
    for volume, unit in sample_volumes:
        print(f"{volume} {unit} is {convert_to_liters(volume, unit)} liters")