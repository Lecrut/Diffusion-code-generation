def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power(-base, -exponent)
    result = 1
    current_base = base
    current_exponent = exponent
    while current_exponent > 0:
        if current_exponent % 2 == 1:
            result *= current_base
        current_base *= current_base
        current_exponent //= 2
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 3))
    print(power(5, 0))
    print(power(2, -3))