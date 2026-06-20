def convert_distance(distance, target_unit, source_unit):
    if distance == 0:
        return 0.0
    
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }
    
    if source_unit not in conversion_factors or target_unit not in conversion_factors:
        raise ValueError(f"Invalid unit. Supported units: {list(conversion_factors.keys())}")
    
    if conversion_factors[target_unit] == 0:
        raise ZeroDivisionError("Cannot convert to a unit with a zero conversion factor.")
    
    base_value = distance * conversion_factors[source_unit]
    result = base_value / conversion_factors[target_unit]
    return result

if __name__ == '__main__':
    distance_input = 100.0
    source_unit_input = 'meters'
    target_unit_input = 'feet'
    
    output_value = convert_distance(distance_input, target_unit_input, source_unit_input)
    print(output_value)