def recursive_power(base, exponent):
    if exponent < 0:
        return 1 / recursive_power(base, -exponent)
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        half = recursive_power(base, exponent // 2)
        return half * half
    return base * recursive_power(base, exponent - 1)

if __name__ == '__main__':
    print(recursive_power(2, 10))
    print(recursive_power(3, 5))
    print(recursive_power(5, -2))
    print(recursive_power(7, 0))
    print(recursive_power(1.5, 3))