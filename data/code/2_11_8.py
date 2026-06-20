def standardize_volume(volumes, base_unit='cubic_meters'):
    conversion_factors = {
        'cubic_meters': 1.0,
        'liters': 0.001,
        'gallons': 0.00378541,
        'cubic_feet': 0.0283168,
        'milliliters': 0.000001,
        'barrels': 0.158987,
    }
    if base_unit not in conversion_factors:
        raise ValueError(f"Unsupported base unit: {base_unit}")
    standardized = {}
    for key, value in volumes.items():
        unit = key.lower()
        if unit in conversion_factors:
            standardized[key] = value * conversion_factors[unit]
        else:
            standardized[key] = value
    return standardized

if __name__ == '__main__':
    sample_volumes = {
        'water_liters': 100.0,
        'sand_cubic_feet': 5.0,
        'oil_gallons': 50.0,
        'gravel_cubic_meters': 2.5
    }
    unit_mapping = {
        'water_liters': 'liters',
        'sand_cubic_feet': 'cubic_feet',
        'oil_gallons': 'gallons',
        'gravel_cubic_meters': 'cubic_meters'
    }
    mapped_volumes = {unit_mapping[k]: v for k, v in sample_volumes.items()}
    result = standardize_volume(mapped_volumes)
    print(result)