def convert_length(length: float, from_unit: str, to_unit: str = None) -> float:
    conversion_factors = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.344
    }
    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {from_unit}")
    if to_unit is None:
        return length
    if to_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {to_unit}")
    meters = length * conversion_factors[from_unit]
    result = meters / conversion_factors[to_unit]
    return result

if __name__ == '__main__':
    result1 = convert_length(100, 'm', 'ft')
    print(result1)
    result2 = convert_length(5, 'km', 'mi')
    print(result2)
    result3 = convert_length(72, 'in', 'cm')
    print(result3)