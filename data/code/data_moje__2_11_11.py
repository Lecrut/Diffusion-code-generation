def standardize_volume(volumes, unit='liters'):
    conversion_factors = {
        'cubic_meters': 1000.0,
        'liters': 1.0,
        'milliliters': 0.001,
        'gallons': 3.78541,
        'cubic_feet': 28.3168,
        'cubic_inches': 0.0163871
    }
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    factor = conversion_factors[unit]
    standardized = {}
    for name, value in volumes.items():
        standardized[name] = value * factor
    return standardized

if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5.5}
    result = standardize_volume(sample_volumes, 'liters')
    print(result)