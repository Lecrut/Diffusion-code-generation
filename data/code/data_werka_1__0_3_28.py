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

    meters = value * units_to_meters[from_unit]
    result = meters / units_to_meters[to_unit]
    return result

if __name__ == '__main__':
    val = 10.0
    src = 'm'
    tgt = 'ft'
    converted = convert_length(val, src, tgt)
    print(converted)