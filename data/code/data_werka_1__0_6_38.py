def convert_length(value, from_unit, to_unit):
    units_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254,
    }

    if from_unit not in units_to_meters:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in units_to_meters:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    meters = value * units_to_meters[from_unit]
    result = meters / units_to_meters[to_unit]
    
    return result

if __name__ == '__main__':
    print(convert_length(1, 'km', 'm'))
    print(convert_length(5280, 'ft', 'mi'))
    print(convert_length(1, 'in', 'cm'))