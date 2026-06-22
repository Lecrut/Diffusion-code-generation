def convert_lengths(measurements, unit):
    conversion_factors = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.34,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters_per_unit = conversion_factors[unit]
    meters_per_foot = 0.3048
    
    results = []
    for value in measurements:
        value_in_meters = value * meters_per_unit
        value_in_feet = value_in_meters / meters_per_foot
        results.append({
            'original': value,
            'unit': unit,
            'meters': value_in_meters,
            'feet': value_in_feet
        })
    return results

if __name__ == '__main__':
    sample_data = [1.5, 10, 0.05, 5280]
    input_unit = 'mi'
    output_data = convert_lengths(sample_data, input_unit)
    for item in output_data:
        print(f"{item['original']} {item['unit']} = {item['meters']} m = {item['feet']} ft")