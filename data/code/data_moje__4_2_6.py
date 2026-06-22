def convert_distance(value, unit):
    factors_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344,
        'ft': 0.3048,
        'in': 0.0254,
        'cm': 0.01,
        'mm': 0.001,
        'yd': 0.9144
    }
    
    if unit not in factors_to_meters:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters = value * factors_to_meters[unit]
    
    results = {}
    for u, factor in factors_to_meters.items():
        results[u] = meters / factor
        
    return results

if __name__ == '__main__':
    result = convert_distance(1, 'km')
    print(result)