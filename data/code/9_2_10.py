def convert_volume(value, target_unit):
    UNIT_FACTORS_TO_LITERS = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.785411784,
        'ml': 0.001,
        'fl_oz': 0.0295735296,
        'cup': 0.236588236,
        'pt': 0.473176473,
        'qt': 0.946352946,
        'tbsp': 0.0147867648,
        'tsp': 0.0049289216,
        'in3': 0.016387064,
        'ft3': 28.316846592
    }
    
    if target_unit not in UNIT_FACTORS_TO_LITERS:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    liters = value * UNIT_FACTORS_TO_LITERS[target_unit]
    return liters

if __name__ == '__main__':
    print(convert_volume(1, 'm3'))
    print(convert_volume(264.172, 'gal'))
    print(convert_volume(500, 'L'))
    print(convert_volume(1, 'fl_oz'))