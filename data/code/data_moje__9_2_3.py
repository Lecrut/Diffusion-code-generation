VOLUME_CONVERSIONS = {
    'L': 1.0,
    'm3': 1000.0,
    'gal': 3.785411784,
    'ml': 0.001,
    'fl_oz': 0.0295735295625,
    'qt': 0.946352946,
    'pt': 0.473176473,
    'cup': 0.24,
    'tbsp': 0.0147867647812,
    'tsp': 0.00492892159375,
    'in3': 0.016387064,
    'ft3': 28.316846592,
}

def convert_volume(value, target_unit):
    if target_unit not in VOLUME_CONVERSIONS:
        raise ValueError(f"Unknown unit: {target_unit}")
    base_value = value * VOLUME_CONVERSIONS[target_unit]
    return base_value

if __name__ == '__main__':
    result1 = convert_volume(5, 'gal')
    result2 = convert_volume(1000, 'L')
    result3 = convert_volume(2.5, 'm3')
    print(result1)
    print(result2)
    print(result3)