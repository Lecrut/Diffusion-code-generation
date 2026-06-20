def convert_distance(distance, unit):
    base_units = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    if unit not in base_units:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters = distance * base_units[unit]
    
    results = {}
    for u, factor in base_units.items():
        results[u] = meters / factor
    
    return results

if __name__ == '__main__':
    result = convert_distance(1, 'km')
    print(result)