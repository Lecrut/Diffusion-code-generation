def convert_length(value, from_unit, to_unit):
    meters_per_unit = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144
    }

    if from_unit not in meters_per_unit:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit not in meters_per_unit:
        raise ValueError(f"Unknown target unit: {to_unit}")

    value_in_meters = value * meters_per_unit[from_unit]
    converted_value = value_in_meters / meters_per_unit[to_unit]
    
    return converted_value

if __name__ == '__main__':
    result = convert_length(100, 'm', 'ft')
    print(result)