def convert_volume_to_liters(volume, unit):
    conversion_factors = {
        'liters': 1.0,
        'milliliters': 0.001,
        'cubic_meters': 1000.0,
        'cubic_centimeters': 0.001,
        'gallons': 3.785411784,
        'quarts': 0.946352946,
        'pints': 0.473176473,
        'fluid_ounces': 0.0295735296,
        'cups': 0.2365882365,
        'tablespoons': 0.0147867648,
        'teaspoons': 0.0049153932
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return volume * conversion_factors[unit]

if __name__ == '__main__':
    sample_volumes = [
        (1, 'liters'),
        (1000, 'milliliters'),
        (1, 'cubic_meters'),
        (1000, 'cubic_centimeters'),
        (1, 'gallons'),
        (1, 'quarts'),
        (1, 'pints'),
        (8, 'fluid_ounces'),
        (2, 'cups'),
        (6, 'tablespoons'),
        (3, 'teaspoons')
    ]
    
    for volume, unit in sample_volumes:
        liters = convert_volume_to_liters(volume, unit)
        print(f"{volume} {unit} is equal to {liters:.10f} liters")