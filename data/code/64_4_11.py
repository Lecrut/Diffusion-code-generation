def recursive_power(base, exponent):
    if exponent < 0:
        return recursive_power(1 / base, -exponent)
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    half = recursive_power(base, exponent // 2)
    if exponent % 2 == 0:
        return half * half
    else:
        return half * half * base

if __name__ == '__main__':
    print(recursive_power(2, 10))
    print(recursive_power(3, 5))
    print(recursive_power(5, 0))
    print(recursive_power(2, -3))