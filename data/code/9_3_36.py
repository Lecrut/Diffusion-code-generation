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
        'gal': 3.78541,
    }
    
    if unit.lower() not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return volume * conversion_factors[unit.lower()]

if __name__ == '__main__':
    sample_values = [
        (250, 'ml'),
        (1.5, 'fl oz'),
        (3, 'cup'),
        (2, 'l'),
        (1, 'gal')
    ]
    
    for volume, unit in sample_values:
        print(f"{volume} {unit} is {convert_to_liters(volume, unit)} liters")