def convert_volume_to_liters(volume, unit):
    conversion_factors = {
        'liters': 1.0,
        'milliliters': 0.001,
        'centiliters': 0.01,
        'deciliters': 0.1,
        'hectoliters': 100.0,
        'kiloliters': 1000.0,
        'cubic meters': 1000.0,
        'cubic centimeters': 0.001,
        'cubic millimeters': 0.000001,
        'gallons': 3.785411784,
        'quarts': 0.946352946,
        'pints': 0.473176473,
        'fluid ounces': 0.0295735296,
        'tablespoons': 0.0147867648,
        'teaspoons': 0.00491588832
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return volume * conversion_factors[unit]

if __name__ == '__main__':
    sample_values = [
        (1, 'liters'),
        (1000, 'milliliters'),
        (50, 'centiliters'),
        (2, 'hectoliters'),
        (1, 'cubic meters'),
        (1000000, 'cubic millimeters'),
        (3.785411784, 'gallons'),
        (1, 'quarts'),
        (2, 'pints'),
        (8, 'fluid ounces'),
        (6, 'tablespoons'),
        (6, 'teaspoons')
    ]
    
    for volume, unit in sample_values:
        print(f"{volume} {unit} is {convert_volume_to_liters(volume, unit)} liters")