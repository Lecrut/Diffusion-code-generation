def convert_to_kilograms(weight_list):
    unit_to_kg = {
        'kg': 1.0,
        'g': 0.001,
        'mg': 0.000001,
        'lb': 0.453592,
        'oz': 0.0283495,
        'ton': 907.185
    }
    
    results = []
    for item in weight_list:
        if not isinstance(item, dict):
            continue
        
        weight = item.get('weight')
        unit = item.get('unit', '').lower()
        
        if weight is None or not isinstance(weight, (int, float)):
            continue
        if unit not in unit_to_kg:
            continue
            
        try:
            kg_value = weight * unit_to_kg[unit]
            results.append({'weight': kg_value, 'unit': 'kg'})
        except (TypeError, ValueError, ZeroDivisionError):
            continue
            
    return results

if __name__ == '__main__':
    measurements = [
        {'weight': 1000, 'unit': 'g'},
        {'weight': 5, 'unit': 'lb'},
        {'weight': 2.5, 'unit': 'kg'},
        {'weight': 'invalid', 'unit': 'kg'},
        {'weight': 100, 'unit': 'unknown'},
        {'weight': 500, 'unit': 'mg'}
    ]
    
    result = convert_to_kilograms(measurements)
    print(result)