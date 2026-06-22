def calculate_power(base, exponent):
    if exponent == 0:
        return 1.0
    if base == 0:
        if exponent > 0:
            return 0.0
        else:
            raise ValueError('0 cannot be raised to a negative power')
    abs_exp = abs(exponent)
    result = 1.0
    current_base = base
    current_exp = abs_exp
    while current_exp > 0:
        if current_exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        current_exp //= 2
    if exponent < 0:
        result = 1.0 / result
    return result
if __name__ == '__main__':
    test_cases = [(2, 10), (5, 0), (2, -2), (3.5, 2), (10, 1), (1, 100), (2.5, -1), (0.5, 3)]
    for base, exp in test_cases:
        output = calculate_power(base, exp)
        print(f'{base}^{exp} = {output}')