def power(base, exponent):
    if exponent < 0:
        return 1 / power(-base if base < 0 else base, -exponent) if base != 0 else 1 / 0
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    half = power(base, exponent // 2)
    result = half * half
    if exponent % 2 == 1:
        result *= base
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 0))
    print(power(2, -3))
    print(power(5, 1))
    print(power(0, 5))
    print(power(-2, 3))
    print(power(2.5, 3))