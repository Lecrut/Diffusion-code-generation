def convert_volume(volume, target_unit):
    conversion_factors = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'ml': 0.001,
        'ft3': 28.3168,
        'cup': 0.24,
        'tbsp': 0.015,
        'tsp': 0.005
    }
    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {target_unit}")
    return volume / conversion_factors[target_unit]

if __name__ == '__main__':
    sample_volume = 1
    sample_units = ['L', 'm3', 'gal', 'ml', 'ft3', 'cup', 'tbsp', 'tsp']
    results = {}
    for unit in sample_units:
        results[unit] = convert_volume(sample_volume, unit)
    print(results)