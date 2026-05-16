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
        return f"Error: Conversion from {length_str} to {target_unit} is not supported"
    if length_str == target_unit:
        return float(length_str)
    factor = conversion_factors[length_str][target_unit]
    try:
        result = float(length_str) * factor
        return result
    except ValueError:
        return f"Error: Invalid numeric value provided for length: {length_str}"
if __name__ == '__main__':
    print(convert_length('10', 'ft'))
    print(convert_length('10', 'm'))
    print(convert_length('10', 'm'))
    print(convert_length('10', 'in'))
    print(convert_length('10', 'yd'))
    print(convert_length('5', 'ft'))
    print(convert_length('10', 'm'))
    print(convert_length('10', 'm'))
    print(convert_length('10', 'm'))
    print(convert_length('10', 'm'))