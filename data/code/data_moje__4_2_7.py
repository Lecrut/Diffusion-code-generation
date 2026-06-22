def convert_distance(value, unit):
    supported_units = ['m', 'km', 'cm', 'mm', 'mi', 'yd', 'ft', 'in']
    if unit not in supported_units:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    base_value = value * meters[unit]
    
    results = {}
    for u in supported_units:
        results[u] = base_value / meters[u]
    
    return results

if __name__ == '__main__':
    sample_value = 1.0
    sample_unit = 'mi'
    output = convert_distance(sample_value, sample_unit)
    print(output)