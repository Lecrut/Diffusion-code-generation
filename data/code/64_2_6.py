def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    if isinstance(exponent, float) or isinstance(base, float):
        return base ** exponent
    result = 1
    current_base = base
    exp = exponent
    while exp > 0:
        if exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        exp //= 2
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(2, -3))
    print(power(2.5, 3))
    print(power(3, 0))
    print(power(1.5, 2.5))