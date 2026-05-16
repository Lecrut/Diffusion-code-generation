def convert_length(length_str, target_unit):
    conversion_map = {
        'm': {'ft': 3.28084},
        'ft': {'m': 0.3048},
        'in': {'ft': 1/12},
        'ft': {'in': 12},
        'yd': {'ft': 3},
        'ft': {'yd': 1/3},
    }
    if length_str not in conversion_map:
        return f"Error: Unknown length unit '{length_str}'"
    if target_unit not in conversion_map[length_str]:
        return f"Error: Cannot convert from {length_str} to {target_unit}"
    factor = conversion_map[length_str][target_unit]
    result = float(length_str) * factor
    return result
if __name__ == '__main__':
    print(convert_length('10', 'ft'))
    print(convert_length('5', 'm'))
    print(convert_length('100', 'in'))
    print(convert_length('1', 'yd'))
    print(convert_length('10', 'm'))
    print(convert_length('10', 'ft'))
    print(convert_length('10', 'cm'))
    print(convert_length('5', 'ft'))