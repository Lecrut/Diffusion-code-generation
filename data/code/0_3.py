def convert_length(value, from_unit, to_unit):
    units_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
    }

    if from_unit not in units_to_meters or to_unit not in units_to_meters:
        raise ValueError("Unsupported unit code provided.")

    if from_unit == to_unit:
        return value

    value_in_meters = value * units_to_meters[from_unit]
    result = value_in_meters / units_to_meters[to_unit]
    return result

if __name__ == '__main__':
    result = convert_length(100, 'm', 'ft')
    print(result)