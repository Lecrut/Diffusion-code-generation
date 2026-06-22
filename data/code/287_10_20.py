conversion_factors = {'kg': 1.0, 'lb': 2.20462, 'g': 1000.0}

def convert_weight(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError('Input value must be a number.')
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError('Units must be provided as strings.')
    if from_unit == to_unit:
        return value
    if from_unit in conversion_factors and to_unit in conversion_factors:
        from_factor = conversion_factors[from_unit]
        to_factor = conversion_factors[to_unit]
        return value / from_factor * to_factor
    else:
        raise ValueError('Unsupported unit provided.')
if __name__ == '__main__':
    print(convert_weight(1, 'kg', 'lb'))
    print(convert_weight(1, 'lb', 'kg'))
    print(convert_weight(1000, 'g', 'kg'))