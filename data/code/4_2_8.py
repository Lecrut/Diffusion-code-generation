def convert_distance(distance, unit):
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    
    if unit == 'm':
        meters = distance
    elif unit == 'km':
        meters = distance * 1000
    elif unit == 'mi':
        meters = distance * 1609.344
    elif unit == 'ft':
        meters = distance * 0.3048
    elif unit == 'cm':
        meters = distance * 0.01
    elif unit == 'mm':
        meters = distance * 0.001
    elif unit == 'in':
        meters = distance * 0.0254
    else:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return {
        'm': meters,
        'km': meters / 1000,
        'mi': meters / 1609.344,
        'ft': meters / 0.3048,
        'cm': meters / 0.01,
        'mm': meters / 0.001,
        'in': meters / 0.0254
    }

if __name__ == '__main__':
    print(convert_distance(1, 'km'))
    print(convert_distance(1, 'mi'))
    print(convert_distance(100, 'm'))