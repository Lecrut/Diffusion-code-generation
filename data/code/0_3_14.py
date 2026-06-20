def convert_length(value, from_unit, to_unit):
    units_to_meters = {
        'm': 1.0,
        'ft': 0.3048,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'yd': 0.9144,
        'km': 1000.0,
        'mi': 1609.344,
        'ft_us': 0.3048006096012192,
        'mi_us': 1609.347218694437,
    }
    if from_unit not in units_to_meters:
        raise ValueError(f"Unsupported from_unit: {from_unit}")
    if to_unit not in units_to_meters:
        raise ValueError(f"Unsupported to_unit: {to_unit}")
    value_in_meters = value * units_to_meters[from_unit]
    converted_value = value_in_meters / units_to_meters[to_unit]
    return converted_value

if __name__ == '__main__':
    result = convert_length(100, 'm', 'ft')
    print(result)
    result = convert_length(1, 'mi', 'km')
    print(result)