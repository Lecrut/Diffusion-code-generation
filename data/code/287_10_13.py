def convert_weight(value: float, from_unit: str, to_unit: str) -> float:
    conversion_factors = {'kg': 1.0, 'g': 1000.0, 'lb': 2.20462, 'oz': 35.2739}
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError('Invalid unit provided.')
    value_in_base = value * conversion_factors[from_unit]
    return value_in_base / conversion_factors[to_unit]
if __name__ == '__main__':
    print(convert_weight(1, 'kg', 'lb'))
    print(convert_weight(500, 'g', 'kg'))