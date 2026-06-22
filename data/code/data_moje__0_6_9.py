def convert_length(value, unit, target_unit):
    conversions = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254,
    }
    
    if unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    if target_unit not in conversions:
        raise ValueError(f"Unsupported target unit: {target_unit}")
        
    meters = value * conversions[unit]
    result = meters / conversions[target_unit]
    return result

if __name__ == '__main__':
    print(convert_length(1, 'km', 'mi'))
    print(convert_length(5280, 'ft', 'mi'))
    print(convert_length(1, 'mi', 'km'))