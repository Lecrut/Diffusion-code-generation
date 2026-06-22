def power(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number.")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be a number.")
    if exponent < 0 and base < 0:
        raise ValueError("Negative base cannot have a negative exponent.")
    if exponent == 0:
        return 1
    if base == 0:
        return 0
    result = 1.0
    is_negative_exp = exponent < 0
    abs_exponent = abs(exponent)
    while abs_exponent > 0:
        if abs_exponent % 1 == 0:
            int_exponent = int(abs_exponent)
            result *= base ** int_exponent
            break
        result *= base
        abs_exponent -= 1
    if is_negative_exp:
        result = 1.0 / result
    return result

if __name__ == '__main__':
    base_val = 2
    exp_val = 10
    val = power(base_val, exp_val)
    print(val)