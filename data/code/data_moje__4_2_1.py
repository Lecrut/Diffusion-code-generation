def convert_distance(value, unit):
    valid_units = {'m', 'km', 'mi', 'ft', 'in', 'cm', 'mm', 'yd'}
    if unit not in valid_units:
        raise ValueError(f"Unsupported unit: {unit}. Supported units: {valid_units}")
    
    meters = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344,
        'ft': 0.3048,
        'in': 0.0254,
        'cm': 0.01,
        'mm': 0.001,
        'yd': 0.9144
    }
    
    base_meters = value * meters[unit]
    
    results = {}
    for u, factor in meters.items():
        results[u] = base_meters / factor
    
    return results

if __name__ == '__main__':
    sample_value = 100
    sample_unit = 'm'
    result = convert_distance(sample_value, sample_unit)
    print(result)
    
    sample_value_mi = 1
    sample_unit_mi = 'mi'
    result_mi = convert_distance(sample_value_mi, sample_unit_mi)
    print(result_mi)