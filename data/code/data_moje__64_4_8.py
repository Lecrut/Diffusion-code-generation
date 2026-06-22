def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    half = power(base, exponent // 2)
    result = half * half
    if exponent % 2 != 0:
        result *= base
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 5))
    print(power(2, 0))
    print(power(2, -3))
    print(power(10, 100))