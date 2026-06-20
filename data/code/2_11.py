def standardize_volume(volumes):
    CONVERSION_TO_CUBIC_METERS = {
        'water': 1.0,
        'sand': 1.0,
        'gallon': 0.00378541,
        'liter': 0.001,
        'cubic_foot': 0.0283168,
        'cubic_yard': 0.764555,
    }

    standardized = {}
    for material, value in volumes.items():
        material_lower = material.lower()
        if material_lower in CONVERSION_TO_CUBIC_METERS:
            factor = CONVERSION_TO_CUBIC_METERS[material_lower]
            standardized[material] = value * factor
        else:
            standardized[material] = value
    return standardized

if __name__ == '__main__':
    sample_data = {'water': 10.0, 'sand': 5.5, 'gallon': 5.0}
    result = standardize_volume(sample_data)
    print(result)