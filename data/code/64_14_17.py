def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    is_negative = exponent < 0
    exp = abs(exponent)
    result = 1
    current_base = base
    while exp > 0:
        if exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        exp //= 2
    if is_negative:
        result = 1 / result
    return result
if __name__ == '__main__':
    test_cases = [(2, 10), (5, 0), (2, -2), (3, 3), (10, -1), (0.5, 2), (-2, 3), (-2, 4)]
    for base, exp in test_cases:
        result = calculate_power(base, exp)
        print(f'{base}^{exp} = {result}')