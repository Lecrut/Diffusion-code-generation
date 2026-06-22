def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    half, rem = divmod(exp, 2)
    res = power(base, half)
    if rem == 0:
        return res * res
    return res * res * base

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 0))
    print(power(5, -2))
    print(power(10, 6))