def recursive_power(base, exponent):
    if exponent < 0:
        return 1 / recursive_power(base, -exponent)
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        half_power = recursive_power(base, exponent // 2)
        return half_power * half_power
    else:
        return base * recursive_power(base, exponent - 1)

if __name__ == '__main__':
    result1 = recursive_power(2, 10)
    print(result1)
    result2 = recursive_power(3, 7)
    print(result2)
    result3 = recursive_power(5, 0)
    print(result3)
    result4 = recursive_power(2, -3)
    print(result4)
    result5 = recursive_power(10, 1)
    print(result5)