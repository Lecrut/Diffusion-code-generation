def is_zero(value):
    if isinstance(value, (int, float)):
        return value == 0
    elif isinstance(value, complex):
        return value == 0 + 0j
    else:
        raise ValueError('Unsupported data type')

if __name__ == '__main__':
    test_values = [0, 0.0, 0 + 0j, 1, 1.5, 1 + 2j, '0', '', None]
    for val in test_values:
        try:
            print(is_zero(val))
        except ValueError as e:
            print(e)