def standardize_volume(volume_dict, conversion_factors=None):
    if conversion_factors is None:
        conversion_factors = {
            'water': 0.001,
            'sand': 0.001,
            'concrete': 0.001,
            'm3': 1.0,
            'liter': 0.001,
            'milliliter': 0.000001,
            'gallon': 0.00378541,
            'cubic_foot': 0.0283168
        }
    
    standardized = {}
    for substance, volume in volume_dict.items():
        factor = conversion_factors.get(substance, 1.0)
        standardized[substance] = volume * factor
    return standardized

if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 5.5, 'concrete': 2.0}
    result = standardize_volume(sample_volumes)
    print(result)