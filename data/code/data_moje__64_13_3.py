def modular_exponentiation(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def large_integer_power(base, exponent, modulus=None):
    if modulus is not None:
        return modular_exponentiation(base, exponent, modulus)
    result = 1
    negative_exponent = exponent < 0
    if negative_exponent:
        if base == 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power")
        base = 1 / base
        exponent = -exponent
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        exponent //= 2
        if exponent > 0:
            base *= base
    return result

if __name__ == '__main__':
    base_val = 2
    exponent_val = 1000
    modulus_val = 1000000007

    mod_result = large_integer_power(base_val, exponent_val, modulus_val)
    print(mod_result)

    non_mod_result = large_integer_power(3, 10)
    print(non_mod_result)

    large_base = 123456789
    large_exp = 987654321
    large_mod = 10**9 + 7
    large_mod_result = large_integer_power(large_base, large_exp, large_mod)
    print(large_mod_result)