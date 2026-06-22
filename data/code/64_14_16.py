def calculate_power(base, exponent):
    if exponent == 0:
        return 1.0

    result = 1.0
    current_exponent = exponent
    is_negative = current_exponent < 0

    if is_negative:
        current_exponent = -current_exponent
        base = 1.0 / base

    while current_exponent > 0:
        if current_exponent % 2 == 1:
            result *= base
        base *= base
        current_exponent //= 2

    return result

if __name__ == '__main__':
    test_cases = [
        (2, 10),
        (5, 0),
        (2, -2),
        (3.5, 3),
        (-2, 3),
        (0, 5),
        (10, -1)
    ]

    for b, e in test_cases:
        value = calculate_power(b, e)
        print(value)