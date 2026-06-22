def power_by_squaring(base, exp):
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
    print(power_by_squaring(2, 10))
    print(power_by_squaring(-3, 3))
    print(power_by_squaring(5, 0))
    print(power_by_squaring(2, -2))