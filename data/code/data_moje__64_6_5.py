def power(base, exponent):
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    result = 1
    while exponent > 0:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 4))
    print(power(5, 0))
    print(power(2, -3))