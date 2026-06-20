def convert_volume(volume, target_unit):
    conversions = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'ml': 0.001,
        'ft3': 28.3168,
        'cup': 0.24,
        'tbsp': 0.0147868,
        'tsp': 0.00492892
    }
    if target_unit not in conversions:
        raise ValueError(f"Unsupported unit: {target_unit}")
    return volume / conversions[target_unit]

if __name__ == '__main__':
    print(convert_volume(1000, 'L'))
    print(convert_volume(1, 'm3'))
    print(convert_volume(5, 'gal'))
    print(convert_volume(100, 'ml'))
    print(convert_volume(2, 'ft3'))
    print(convert_volume(8, 'cup'))
    print(convert_volume(16, 'tbsp'))
    print(convert_volume(48, 'tsp'))