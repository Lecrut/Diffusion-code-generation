def convert_length(length_str, target_unit):
    conversion_factors = {
        'm': {'ft': 3.28084},
        'ft': {'m': 0.3048},
        'in': {'ft': 1/12},
        'ft': {'in': 12},
        'yd': {'ft': 3},
        'ft': {'yd': 1/3},
    }
    if length_str not in conversion_factors:
        return f"Error: Unknown length unit '{length_str}'"
    if target_unit not in conversion_factors[length_str]:
        return f"Error: Cannot convert from {length_str} to {target_unit}"
    factor = conversion_factors[length_str][target_unit]
    try:
        result = float(length_str) * factor
        return result
    except ValueError:
        return "Error: Invalid numeric value provided for length."
if __name__ == '__main__':
    print(convert_length('10', 'ft'))
    print(convert_length('5', 'm'))
    print(convert_length('100', 'yd'))
    print(convert_length('12', 'in'))
    print(convert_length('10', 'm'))
    print(convert_length('10', 'm_invalid'))
    print(convert_length('abc', 'ft'))