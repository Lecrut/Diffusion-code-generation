def power(base, exponent):
    if exponent < 0:
        return 1 / _power_positive(base, -exponent)
    return _power_positive(base, exponent)

def _power_positive(base, exponent):
    result = 1
    current_base = base
    current_exp = exponent
    while current_exp > 0:
        if current_exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        current_exp //= 2
    return result

if __name__ == '__main__':
    print(power(2, 10))
    print(power(3, 0))
    print(power(5, -2))
    print(power(10, 3))
    print(power(0, 5))
    print(power(7, 1))