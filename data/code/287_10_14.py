def convert_weight(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError('Input value must be a number.')
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError('Units must be provided as strings.')
    conversion_factors = {'kg': 1.0, 'g': 1000.0, 'lb': 2.20462, 'oz': 35.2739}
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError('Invalid unit provided.')
    value_in_base = value * conversion_factors[from_unit]
    return value_in_base / conversion_factors[to_unit]
if __name__ == '__main__':
    print(convert_weight(1, 'kg', 'lb'))
    print(convert_weight(1, 'g', 'kg'))