def standardize_volume(volumes):
    conversion_factors = {
        'cubic_meters': 1.0,
        'liters': 0.001,
        'milliliters': 0.000001,
        'gallons': 0.00378541,
        'cubic_feet': 0.0283168,
        'cubic_inches': 0.0000163871,
        'imperial_gallons': 0.00454609,
        'barrels': 0.158987,
        'fluid_ounces': 0.0000295735,
        'cups': 0.000236588,
        'pints': 0.000473176,
        'quarts': 0.000946353
    }
    standardized = {}
    for key, value in volumes.items():
        unit = key.lower()
        if unit not in conversion_factors:
            standardized[key] = None
        else:
            standardized[key] = value * conversion_factors[unit]
    return standardized

if __name__ == '__main__':
    sample_volumes = {
        'water_liters': 10.0,
        'sand_cubic_feet': 5.5,
        'oil_gallons': 2.5,
        'juice_milliliters': 500.0
    }
    result = standardize_volume(sample_volumes)
    print(result)