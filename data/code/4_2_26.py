def convert_distance(distance, unit):
    conversion_factors = {
        'm': {'km': 0.001, 'mi': 0.000621371},
        'km': {'m': 1000, 'mi': 0.621371},
        'mi': {'m': 1609.34, 'km': 1.60934}
    }
    
    if unit not in conversion_factors:
        raise ValueError("Unsupported unit")
    
    result = {}
    for target_unit, factor in conversion_factors[unit].items():
        result[target_unit] = distance * factor
    
    return result

if __name__ == '__main__':
    sample_distance = 10
    sample_unit = 'km'
    converted_distances = convert_distance(sample_distance, sample_unit)
    print(converted_distances)