def convert_length(value_str, target_unit):
    units_to_meters = {'m': 1.0, 'km': 1000.0, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.344, 'ft': 0.3048, 'in': 0.0254, 'yd': 0.9144}
    target_unit = target_unit.strip().lower()
    try:
        value = float(value_str)
    except ValueError:
        import re
        match = re.match('^([+-]?\\d*\\.?\\d+)\\s*([a-zA-Z]*)$', value_str)
        if match:
            value = float(match.group(1))
            input_unit = match.group(2).lower() if match.group(2) else None
        else:
            raise ValueError(f'Invalid length string: {value_str}')
    else:
        input_unit = None
    if 'input_unit' in locals() and input_unit is not None:
        if input_unit not in units_to_meters:
            raise ValueError(f'Unknown source unit: {input_unit}')
    else:
        input_unit = 'm'
    if target_unit not in units_to_meters:
        raise ValueError(f'Unknown target unit: {target_unit}')
    value_in_meters = value * units_to_meters[input_unit]
    result = value_in_meters / units_to_meters[target_unit]
    return result
if __name__ == '__main__':
    result1 = convert_length('1 m', 'ft')
    print(f'1 meter is {result1} feet')
    result2 = convert_length('5 km', 'mi')
    print(f'5 kilometers is {result2} miles')
    result3 = convert_length('12 in', 'cm')
    print(f'12 inches is {result3} centimeters')
    result4 = convert_length('6.5 ft', 'm')
    print(f'6.5 feet is {result4} meters')