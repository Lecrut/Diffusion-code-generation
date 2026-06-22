def convert_to_liters(volume, unit):
    conversion_factors = {
        'ml': 1e-3,
        'cl': 1e-2,
        'dl': 1e-1,
        'l': 1.0,
        'gal': 3.785411784,
        'qt': 0.946352946,
        'pt': 0.473176473,
        'fl oz': 0.02957352956,
        'tsp': 0.004928921594,
        'teaspoon': 0.004928921594,
        'tablespoon': 0.01478676478,
        'cup': 0.2365882365,
        'pint': 0.473176473,
        'quart': 0.946352946,
        'gallon': 3.785411784
    }
    
    if unit.lower() not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return volume * conversion_factors[unit.lower()]

if __name__ == '__main__':
    sample_values = [
        (100, 'ml'),
        (2, 'cl'),
        (5, 'dl'),
        (3.785411784, 'gal'),
        (16, 'fl oz')
    ]
    
    for volume, unit in sample_values:
        print(f"{volume} {unit} is {convert_to_liters(volume, unit)} liters")