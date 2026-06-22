def power(base, exponent):
    if exponent < 0:
        return 1 / _power_helper(base, -exponent)
    return _power_helper(base, exponent)

def _power_helper(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 1:
        return base * _power_helper(base, exp - 1)
    half = _power_helper(base, exp // 2)
    return half * half

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 0))
    print(power(2, -3))
    print(power(5, 3))
    print(power(1.5, 2))
    print(power(10, 5))
    print(power(7, 1))
    print(power(0, 5))
    print(power(4, -2))
    print(power(1, 100))