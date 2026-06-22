def power(base, exponent):
    if exponent < 0:
        return 1 / power(base, -exponent)
    if exponent == 0:
        return 1
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(5, 0))
    print(power(3, 5))