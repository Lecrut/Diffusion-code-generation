def convert_distance(distance, unit):
    units = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    if unit not in units:
        raise ValueError(f"Unsupported unit: {unit}")
    
    distance_in_meters = distance * units[unit]
    
    result = {}
    for u, factor in units.items():
        if u != unit:
            result[u] = distance_in_meters / factor
    
    return result

if __name__ == '__main__':
    sample_distance = 5.0
    sample_unit = 'km'
    converted = convert_distance(sample_distance, sample_unit)
    print(converted)