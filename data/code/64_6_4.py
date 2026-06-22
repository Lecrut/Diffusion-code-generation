def power(base, exp):
    if exp < 0:
        base = 1 / base
        exp = -exp
    result = 1
    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(5, 3))
    print(power(10, 0))