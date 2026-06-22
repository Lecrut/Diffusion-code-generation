def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        base = 1 / base
        exp = -exp
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 5))
    print(power(-2, 3))
    print(power(-3, 4))
    print(power(5, -2))