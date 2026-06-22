def convert_to_kg(weight_list):
    results = []
    conversions = {
        'kg': 1.0,
        'g': 0.001,
        'mg': 0.000001,
        'lb': 0.453592,
        'oz': 0.0283495,
        't': 1000.0,
        'ton': 1000.0,
        'stone': 6.35029
    }
    for item in weight_list:
        if isinstance(item, dict):
            weight_val = item.get('value', None)
            unit = item.get('unit', '').lower()
        else:
            parts = str(item).split()
            if len(parts) == 2:
                try:
                    weight_val = float(parts[0])
                    unit = parts[1].lower()
                except ValueError:
                    results.append(None)
                    continue
            elif isinstance(item, (int, float)):
                results.append(float(item))
                continue
            else:
                results.append(None)
                continue
        
        if weight_val is None:
            results.append(None)
            continue
            
        if unit not in conversions:
            results.append(None)
            continue
            
        try:
            kg_val = weight_val * conversions[unit]
            results.append(kg_val)
        except Exception:
            results.append(None)
            
    return results

if __name__ == '__main__':
    measurements = [
        {'value': 1000, 'unit': 'g'},
        {'value': 2.5, 'unit': 'kg'},
        {'value': 50, 'unit': 'lb'},
        {'value': 100, 'unit': 'oz'},
        {'value': 1, 'unit': 'ton'},
        '10 kg',
        '2000 mg',
        {'value': 'invalid', 'unit': 'kg'},
        {'value': 10, 'unit': 'km'},
        5.5
    ]
    converted = convert_to_kg(measurements)
    print(converted)