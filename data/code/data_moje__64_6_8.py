def power_by_squaring(base, exponent):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result

def power(base, exponent):
    if exponent < 0:
        return 1 / power_by_squaring(base, -exponent)
    return power_by_squaring(base, exponent)

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 5))
    print(power(7, 0))
    print(power(5, -2))