def power(base, exponent):
    if exponent < 0:
        raise ValueError("Negative exponents not supported in this integer implementation")
    if exponent == 0:
        return 1
    result = 1
    while exponent > 0:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result

if __name__ == '__main__':
    base_value = 2
    exponent_value = 10
    computed_result = power(base_value, exponent_value)
    print(computed_result)
    print(power(3, 5))
    print(power(5, 0))