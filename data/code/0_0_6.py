def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    unit_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }

    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()

    if from_unit_lower not in unit_to_meters:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in unit_to_meters:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    value_in_meters = value * unit_to_meters[from_unit_lower]
    converted_value = value_in_meters / unit_to_meters[to_unit_lower]

    return converted_value

if __name__ == '__main__':
    result1 = convert_length(1, 'mi', 'km')
    print(result1)

    result2 = convert_length(100, 'cm', 'in')
    print(result2)

    result3 = convert_length(5.5, 'ft', 'm')
    print(result3)

    result4 = convert_length(10, 'km', 'mi')
    print(result4)

    result5 = convert_length(24, 'in', 'cm')
    print(result5)