def convert_length(length_str, target_unit):
    conversion_factors = {
        'm': {'ft': 3.28084},
        'ft': {'m': 0.3048},
        'in': {'m': 0.0254},
        'm': {'in': 39.3701},
        'ft': {'in': 12.000000000000002},
    }
    if length_str not in conversion_factors:
        return f"Error: Unknown length unit '{length_str}'"
    if target_unit not in conversion_factors[length_str]:
        return f"Error: Unknown target unit '{target_unit}' for length '{length_str}'"
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
    print(convert_length('5', 'm'))
    print(convert_length('100', 'in'))
    print(convert_length('1', 'm'))
    print(convert_length('10', 'm'))
    print(convert_length('5', 'ft'))
    print(convert_length('10', 'ft'))
    print(convert_length('10', 'm'))