def convert_distance(distance, target_unit):
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    
    conversion_factors = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
    }
    
    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {target_unit}")
    
    if target_unit == 'm':
        return distance
    else:
        meters = distance / conversion_factors[target_unit]
        return meters

if __name__ == '__main__':
    sample_distance = 5.0
    sample_unit = 'km'
    result = convert_distance(sample_distance, sample_unit)
    print(result)