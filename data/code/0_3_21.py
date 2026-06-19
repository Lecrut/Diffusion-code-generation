def convert_length(value, from_unit, to_unit):
    units_to_meters = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'mi': 1609.344,
        'yd': 0.9144
    }

    if from_unit not in units_to_meters:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit not in units_to_meters:
        raise ValueError(f"Unknown target unit: {to_unit}")

    value_in_meters = value * units_to_meters[from_unit]
    converted_value = value_in_meters / units_to_meters[to_unit]
    
    return converted_value

if __name__ == '__main__':
    result = convert_length(10, 'm', 'ft')
    print(result)