def convert_length(value_str, unit_code):
    units = {
        'mm': 0.001,
        'cm': 0.01,
        'dm': 0.1,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
    }

    if unit_code not in units:
        raise ValueError(f"Unsupported unit code: {unit_code}")

    try:
        value = float(value_str)
    except ValueError:
        raise ValueError(f"Invalid numeric value: {value_str}")

    meters = value * units[unit_code]
    result = meters / units['m']
    return result

if __name__ == '__main__':
    result = convert_length('100', 'cm')
    print(result)