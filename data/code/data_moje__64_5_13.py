def mod_pow(base, exponent, modulus=None):
    if modulus is None:
        return pow(base, exponent)
    return pow(base, exponent, modulus)

if __name__ == '__main__':
    print(mod_pow(2, 10))
    print(mod_pow(3, 7, 5))
    print(mod_pow(5, 3, 100))