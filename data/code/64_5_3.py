def fast_pow(base, exponent, modulus=None):
    if modulus is None:
        return pow(base, exponent)
    return pow(base, exponent, modulus)

if __name__ == '__main__':
    b = 2
    e = 10
    m = 1000
    result_without_mod = fast_pow(b, e)
    result_with_mod = fast_pow(b, e, m)
    print(result_without_mod)
    print(result_with_mod)