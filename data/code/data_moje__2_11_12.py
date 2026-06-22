CONVERSION_FACTORS = {
    'cubic_meter': 1.0,
    'liter': 0.001,
    'cubic_foot': 0.0283168,
    'gallon_us': 0.00378541,
    'cubic_centimeter': 1e-6,
    'milliliter': 1e-6
}

def standardize_volume(measurements, target_unit='cubic_meter', unit_map=None):
    if unit_map is None:
        unit_map = {k: k for k in measurements.keys()}
    
    result = {}
    
    for name, value in measurements.items():
        unit = unit_map.get(name, 'cubic_meter')
        
        if unit not in CONVERSION_FACTORS:
            raise ValueError(f"Unknown unit: {unit} for item {name}")
        
        factor = CONVERSION_FACTORS[unit]
        standardized_value = value * factor
        result[name] = standardized_value
        
    return result

if __name__ == '__main__':
    sample_data = {
        'water': 1000.0,
        'oil': 500.0,
        'gasoline': 2.5
    }
    
    sample_units = {
        'water': 'liter',
        'oil': 'gallon_us',
        'gasoline': 'cubic_foot'
    }
    
    standardized = standardize_volume(sample_data, 'cubic_meter', sample_units)
    print(standardized)