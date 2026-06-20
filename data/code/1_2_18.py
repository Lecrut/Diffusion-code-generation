def convert_weights_to_kg(weight_measurements):
    conversion_factors = {
        'g': 0.001,
        'kg': 1.0,
        'lb': 0.453592,
        'oz': 0.0283495,
        'ton': 907.185
    }
    
    results = []
    
    for measurement in weight_measurements:
        try:
            if not isinstance(measurement, (dict, tuple, list)):
                raise ValueError("Invalid measurement format")
            
            if isinstance(measurement, dict):
                value = measurement.get('value')
                unit = measurement.get('unit', '').lower()
            else:
                if len(measurement) != 2:
                    raise ValueError("Invalid measurement format")
                value, unit = measurement
                unit = str(unit).lower()
            
            if not isinstance(value, (int, float)):
                raise ValueError("Weight value must be numeric")
            
            if value < 0:
                raise ValueError("Weight cannot be negative")
            
            if unit not in conversion_factors:
                raise ValueError(f"Unknown unit: {unit}")
            
            kg_value = value * conversion_factors[unit]
            results.append(kg_value)
        except Exception as e:
            results.append(None)
    
    return results

if __name__ == '__main__':
    sample_measurements = [
        {'value': 100, 'unit': 'g'},
        (5.5, 'kg'),
        [150, 'lb'],
        {'value': 32, 'unit': 'oz'},
        (2, 'ton'),
        {'value': -10, 'unit': 'kg'},
        (100, 'invalid_unit'),
        'malformed_data',
        {'value': 'abc', 'unit': 'kg'},
        (0, 'g')
    ]
    
    converted = convert_weights_to_kg(sample_measurements)
    print(converted)