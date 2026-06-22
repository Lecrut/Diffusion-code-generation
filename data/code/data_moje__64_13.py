def power(base: int, exponent: int, modulus: int | None=None) -> int:
    if exponent < 0:
        if base == 0:
            raise ValueError('0 cannot be raised to a negative power')
        if modulus is not None:
            inv_base = pow(base, -1, modulus)
            base = inv_base
            exponent = -exponent
        else:
            result = 1 / base ** (-exponent)
            if modulus is None:
                return result
    elif exponent == 0:
        return 1 if modulus is None else 1 % modulus
    if modulus is not None:
        result = 1
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = result * base % modulus
            exponent = exponent >> 1
            base = base * base % modulus
        return result
    else:
        return base ** exponent
if __name__ == '__main__':
    result_mod = power(2, 10, 1024)
    result_no_mod = power(2, 100)
    result_large_exp = power(3, 19, 1000000007)
    result_frac = power(2, -2)
    print(result_mod)
    print(result_no_mod)
    print(result_large_exp)
    print(result_frac)