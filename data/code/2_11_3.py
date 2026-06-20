VOLUME_CONVERSION_TO_CUBIC_METERS = {
    'cubic_meter': 1.0,
    'liter': 0.001,
    'milliliter': 1e-6,
    'gallon_us': 0.003785411784,
    'cubic_foot': 0.028316846592,
}

def standardize_volume(measurements):
    standardized = {}
    for item_name, item in measurements.items():
        if isinstance(item, dict):
            value = item.get('value', 0.0)
            unit = item.get('unit', 'cubic_meter')
        else:
            value = float(item)
            unit = 'cubic_meter'
        
        factor = VOLUME_CONVERSION_TO_CUBIC_METERS.get(unit.lower())
        if factor is None:
            raise ValueError(f"Unknown unit: {unit}")
        
        standardized[item_name] = value * factor
    
    return standardized

if __name__ == '__main__':
    sample_data = {
        'water': 1000.0,
        'sand': {'value': 5.5, 'unit': 'cubic_foot'},
        'oil': {'value': 20.0, 'unit': 'gallon_us'},
        'gas': {'value': 500.0, 'unit': 'liter'}
    }
    result = standardize_volume(sample_data)
    print(result)