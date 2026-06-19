def convert_to_liters(volume, unit):
    conversion_factors = {
        'ml': 0.001,
        'cl': 0.01,
        'dl': 0.1,
        'l': 1.0,
        'fl oz': 0.0295735,
        'cup': 0.236588,
        'pt': 0.473176,
        'qt': 0.946353,
        'gal': 3.78541
    }
    
    if unit.lower() not in conversion_factors:
        raise ValueError("Unsupported unit")
    
    return volume * conversion_factors[unit.lower()]

if __name__ == '__main__':
    sample_volumes = [
        (1000, 'ml'),
        (50, 'cl'),
        (2, 'dl'),
        (1, 'l'),
        (8, 'fl oz'),
        (2, 'cup'),
        (1, 'pt'),
        (1, 'qt'),
        (1, 'gal')
    ]
    
    for volume, unit in sample_volumes:
        print(f"{volume} {unit} is {convert_to_liters(volume, unit)} liters")