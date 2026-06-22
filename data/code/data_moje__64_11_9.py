def power(base, exp):
    if exp == 0:
        return 1
    negative = False
    if exp < 0:
        negative = True
        exp = -exp
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    if negative:
        return 1 / result
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(-2, 10))
    print(power(3, -3))
    print(power(-3, -3))
    print(power(5, 0))
    print(power(-5, 0))
    print(power(2, 1))
    print(power(-2, 1))