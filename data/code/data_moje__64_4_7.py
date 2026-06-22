def power(base, exponent):
    result = 1
    current_base = base
    exp = abs(exponent)

    while exp > 0:
        if exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        exp //= 2

    if exponent < 0:
        result = 1 / result

    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, -2))
    print(power(5, 0))
    print(power(10, 5))
    print(power(0.5, 4))