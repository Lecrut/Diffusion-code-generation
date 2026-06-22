def calculate_power(base, exponent):
    if exponent == 0:
        return 1.0

    is_negative_exponent = exponent < 0
    abs_exponent = abs(exponent)

    result = 1.0
    current_base = float(base)
    current_exp = abs_exponent

    while current_exp > 0:
        if current_exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        current_exp //= 2

    if is_negative_exponent:
        result = 1.0 / result

    return result

if __name__ == '__main__':
    print(calculate_power(2, 10))
    print(calculate_power(5, 0))
    print(calculate_power(2, -2))
    print(calculate_power(1.5, 3))
    print(calculate_power(0, 5))
    print(calculate_power(3, 4))