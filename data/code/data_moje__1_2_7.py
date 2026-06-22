def convert_to_kg(measurements):
    result = []
    for item in measurements:
        if not isinstance(item, (int, float)):
            if not isinstance(item, dict):
                continue
            value = item.get('value', 0)
            unit = item.get('unit', '').lower()
        else:
            value = item
            unit = 'kg'
        
        try:
            value = float(value)
        except (ValueError, TypeError):
            continue
        
        unit = unit.replace('s', 'es') if unit.endswith('s') else unit
        if unit.endswith('es'):
            unit = unit[:-2] + 's' if len(unit) > 2 else unit
        
        if unit in ('g', 'gram', 'grams'):
            kg = value / 1000.0
        elif unit in ('mg', 'milligram', 'milligrams'):
            kg = value / 1000000.0
        elif unit in ('oz', 'ounce', 'ounces'):
            kg = value * 0.0283495
        elif unit in ('lb', 'lbs', 'pound', 'pounds'):
            kg = value * 0.453592
        elif unit in ('kg', 'kilogram', 'kilograms'):
            kg = value
        else:
            kg = 0.0
        
        result.append(kg)
    return result

if __name__ == '__main__':
    data = [
        {'value': 1000, 'unit': 'g'},
        50,
        {'value': '1.5', 'unit': 'kg'},
        {'value': '10', 'unit': 'oz'},
        2.5
    ]
    converted = convert_to_kg(data)
    print(converted)