def convert_distance(value, unit):
    units = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344,
        'ft': 0.3048,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'yd': 0.9144
    }
    
    value_in_meters = value * units[unit]
    
    result = {}
    for u, factor in units.items():
        result[u] = value_in_meters / factor
        
    return result

if __name__ == '__main__':
    print(convert_distance(1, 'km'))