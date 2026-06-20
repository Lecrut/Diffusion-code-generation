def convert_volume(value, target_unit):
    unit_factors = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'ml': 0.001,
        'ft3': 28.3168,
        'cup': 0.24,
        'tsp': 0.00492892,
        'tbsp': 0.0147868
    }
    if target_unit not in unit_factors:
        raise ValueError(f"Unsupported unit: {target_unit}")
    return value * unit_factors[target_unit]

if __name__ == '__main__':
    sample_value = 5
    sample_unit = 'gal'
    converted = convert_volume(sample_value, sample_unit)
    print(converted)