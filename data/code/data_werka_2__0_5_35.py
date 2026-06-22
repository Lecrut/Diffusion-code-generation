def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError('Unsupported unit')
    
    value_in_meters = value * conversion_factors[from_unit]
    converted_value = value_in_meters / conversion_factors[to_unit]
    return converted_value

if __name__ == '__main__':
    length_value = 250
    from_unit = 'mm'
    to_unit = 'm'
    result = convert_length(length_value, from_unit, to_unit)
    print(result)