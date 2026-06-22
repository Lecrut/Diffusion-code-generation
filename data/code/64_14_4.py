def calculate_power(base: float, exponent: int) -> float:
    if exponent == 0:
        return 1.0

    negative_exponent = exponent < 0
    exp = abs(exponent)

    result = 1.0
    current_base = base

    while exp > 0:
        if exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        exp //= 2

    if negative_exponent:
        return 1.0 / result

    return result

if __name__ == '__main__':
    test_cases = [
        (2, 10),
        (5, 0),
        (2, -2),
        (3, 5),
        (10, -3),
        (0.5, 3),
        (7, 1),
        (-2, 3),
        (-2, 4)
    ]

    for base, exponent in test_cases:
        result = calculate_power(base, exponent)
        print(f"{base}^{exponent} = {result}")