def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

if __name__ == '__main__':
    test_cases = [
        (2, 10),
        (3, 5),
        (-2, 3),
        (-3, 2),
        (5, 0),
        (2, -2),
    ]
    for base, exp in test_cases:
        print(power(base, exp))