def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / calculate_power(base, -exponent)
    result = 1
    current_power = 1
    current_base = base
    while current_power <= exponent:
        if (exponent >> current_power) & 1:
            result *= current_base
        current_base *= current_base
        current_power += 1
    return result

if __name__ == '__main__':
    print(calculate_power(2, 10))
    print(calculate_power(5, 0))
    print(calculate_power(2, -2))
    print(calculate_power(3, 3))
    print(calculate_power(0.5, 3))
    print(calculate_power(-2, 4))
    print(calculate_power(10, -1))
    print(calculate_power(7, 1))
    print(calculate_power(1.1, 2))
    print(calculate_power(0, 5))