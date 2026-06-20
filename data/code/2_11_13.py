conversion_factors = {
    'cubic_meters': 1.0,
    'liters': 0.001,
    'gallons': 0.00378541,
    'cubic_feet': 0.0283168,
    'milliliters': 1e-6
}

def standardize_volume(volume_data, unit='liters'):
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    factor = conversion_factors[unit]
    standardized = {
        key: value * factor 
        for key, value in volume_data.items()
    }
    
    return standardized

if __name__ == '__main__':
    sample_volumes = {
        'water': 10.0,
        'sand': 5.5,
        'oil': 8.2
    }
    
    result = standardize_volume(sample_volumes, 'liters')
    print(result)