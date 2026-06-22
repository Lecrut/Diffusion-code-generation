def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(base, -exponent)
    if exponent % 2 == 0:
        half = power(base, exponent // 2)
        return half * half
    else:
        return base * power(base, exponent - 1)

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 5))
    print(power(2, -3))
    print(power(5, 0))
    print(power(1.5, 4))