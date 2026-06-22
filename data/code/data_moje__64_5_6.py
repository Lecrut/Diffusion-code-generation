def fast_pow(base, exponent, modulus=None):
    if modulus is None:
        return pow(base, exponent)
    return pow(base, exponent, modulus)

if __name__ == '__main__':
    base = 2
    exponent = 10
    modulus = 1000
    result = fast_pow(base, exponent, modulus)
    print(result)