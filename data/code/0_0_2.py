def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    conversion_factors_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.344,
        'nm': 1e-9,
        'um': 1e-6
    }

    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()

    if from_unit_lower not in conversion_factors_to_meters:
        raise ValueError(f"Unsupported from_unit: {from_unit}")
    if to_unit_lower not in conversion_factors_to_meters:
        raise ValueError(f"Unsupported to_unit: {to_unit}")

    value_in_meters = value * conversion_factors_to_meters[from_unit_lower]
    converted_value = value_in_meters / conversion_factors_to_meters[to_unit_lower]

    return converted_value

if __name__ == '__main__':
    result1 = convert_length(1.0, 'm', 'ft')
    print(result1)

    result2 = convert_length(5.0, 'km', 'mi')
    print(result2)

    result3 = convert_length(100.0, 'cm', 'in')
    print(result3)

    result4 = convert_length(1.0, 'ft', 'm')
    print(result4)

    result5 = convert_length(2.5, 'mi', 'km')
    print(result5)