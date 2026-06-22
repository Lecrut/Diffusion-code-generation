def standardize_volume(measurements):
    conversion_factors = {
        'cubic_meter': 1.0,
        'liter': 0.001,
        'gallon': 0.00378541,
        'cubic_foot': 0.0283168,
        'cup': 0.000236588,
        'milliliter': 0.000001
    }
    
    standardized = {}
    for substance, value in measurements.items():
        if isinstance(value, dict):
            if 'value' not in value or 'unit' not in value:
                raise ValueError(f"Invalid format for substance {substance}")
            raw_value = value['value']
            unit = value['unit']
        else:
            raw_value = value
            unit = 'cubic_meter'
        
        if unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        
        converted_value = raw_value * conversion_factors[unit]
        standardized[substance] = converted_value
    
    return standardized

if __name__ == '__main__':
    sample_data = {
        'water': {'value': 10.0, 'unit': 'liter'},
        'sand': 5.5,
        'oil': {'value': 2.0, 'unit': 'gallon'},
        'gravel': {'value': 1.5, 'unit': 'cubic_foot'}
    }
    result = standardize_volume(sample_data)
    print(result)