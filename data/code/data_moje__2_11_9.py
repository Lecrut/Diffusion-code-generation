def standardize_volume(volumes):
    CONVERSION_TO_M3 = {
        'ml': 1e-6,
        'L': 1e-3,
        'gal': 0.00378541,
        'ft3': 0.0283168,
        'in3': 1.63871e-5,
    }
    
    standardized = {}
    for substance, measurement in volumes.items():
        if isinstance(measurement, dict):
            unit = measurement.get('unit', 'L')
            value = measurement.get('value', 0.0)
        elif isinstance(measurement, (int, float)):
            unit = 'L'
            value = measurement
        else:
            continue
            
        factor = CONVERSION_TO_M3.get(unit, 1.0)
        standardized[substance] = value * factor
        
    return standardized

if __name__ == '__main__':
    sample_volumes = {
        'water': {'value': 10.0, 'unit': 'L'},
        'sand': {'value': 5.5, 'unit': 'gal'},
        'air': 50.0
    }
    
    result = standardize_volume(sample_volumes)
    print(result)