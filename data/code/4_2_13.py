def convert_distance(value, unit):
    if unit == 'm':
        base = value
    elif unit == 'km':
        base = value * 1000.0
    elif unit == 'cm':
        base = value * 0.01
    elif unit == 'mm':
        base = value * 0.001
    elif unit == 'mi':
        base = value * 1609.344
    elif unit == 'ft':
        base = value * 0.3048
    elif unit == 'in':
        base = value * 0.0254
    else:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return {
        'm': base,
        'km': base / 1000.0,
        'cm': base / 0.01,
        'mm': base / 0.001,
        'mi': base / 1609.344,
        'ft': base / 0.3048,
        'in': base / 0.0254
    }

if __name__ == '__main__':
    result = convert_distance(1, 'km')
    print(result)