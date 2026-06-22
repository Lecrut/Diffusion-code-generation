def convert_length(value, from_unit, to_unit):
    conversions = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.344,
    }

    if from_unit not in conversions:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit not in conversions:
        raise ValueError(f"Unknown target unit: {to_unit}")

    meters = value * conversions[from_unit]
    result = meters / conversions[to_unit]
    return result

if __name__ == '__main__':
    value = 100
    from_unit = 'm'
    to_unit = 'ft'
    result = convert_length(value, from_unit, to_unit)
    print(result)