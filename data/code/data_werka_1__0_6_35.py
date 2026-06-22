def convert_length(value, from_unit, to_unit):
    units_in_meters = {
        'mm': 0.001,
        'cm': 0.01,
        'dm': 0.1,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }

    if from_unit not in units_in_meters:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in units_in_meters:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    value_in_meters = value * units_in_meters[from_unit]
    converted_value = value_in_meters / units_in_meters[to_unit]
    
    return converted_value

if __name__ == '__main__':
    result = convert_length(1, 'km', 'mi')
    print(result)