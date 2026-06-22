def convert_length(value, from_unit, to_unit):
    base_units = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254,
    }

    if from_unit not in base_units or to_unit not in base_units:
        raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

    value_in_meters = value * base_units[from_unit]
    converted_value = value_in_meters / base_units[to_unit]
    
    return converted_value

if __name__ == '__main__':
    result = convert_length(1, 'km', 'm')
    print(result)
    
    result2 = convert_length(5280, 'ft', 'mi')
    print(result2)
    
    result3 = convert_length(1, 'in', 'cm')
    print(result3)