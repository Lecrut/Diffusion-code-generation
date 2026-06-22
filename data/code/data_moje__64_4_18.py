def fast_power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / fast_power(base, -exponent)
    if exponent % 2 == 0:
        half = fast_power(base, exponent // 2)
        return half * half
    return base * fast_power(base, exponent - 1)

if __name__ == '__main__':
    base_value = 2
    exp_value = 100
    result = fast_power(base_value, exp_value)
    print(result)