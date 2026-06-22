def convert_length(value, unit_from, unit_to):
    if value < 0:
        raise ValueError("Value cannot be negative")
    if unit_from == unit_to:
        return value

    to_meters = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
    }

    if unit_from not in to_meters or unit_to not in to_meters:
        raise ValueError("Unsupported unit code")

    meters = value * to_meters[unit_from]
    return meters / to_meters[unit_to]

if __name__ == '__main__':
    result = convert_length(1, 'mi', 'km')
    print(result)