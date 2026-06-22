def fast_pow(base, exponent, modulus=None):
    if modulus is None:
        return pow(base, exponent)
    return pow(base, exponent, modulus)

if __name__ == '__main__':
    result1 = fast_pow(2, 10)
    print(result1)
    result2 = fast_pow(3, 7, 100)
    print(result2)
    result3 = fast_pow(5, 3)
    print(result3)