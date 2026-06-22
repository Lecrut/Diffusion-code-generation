def convert_volume(value, target_unit):
    conversion_factors = {
        'L': 1.0,
        'ml': 1000.0,
        'm3': 0.001,
        'gal': 0.264172,
        'qt': 1.05669,
        'pt': 2.11338,
        'cup': 4.22675,
        'fl_oz': 33.814,
        'tbsp': 67.628,
        'tsp': 202.884
    }

    normalized_target = target_unit.lower()

    if normalized_target not in conversion_factors:
        raise ValueError(f"Unsupported unit: {target_unit}")

    return value / conversion_factors[normalized_target]

if __name__ == '__main__':
    sample_value = 5.0
    sample_units = ['L', 'm3', 'gal', 'ml', 'qt']

    for unit in sample_units:
        converted = convert_volume(sample_value, unit)
        print(f"{sample_value} L to {unit}: {converted}")