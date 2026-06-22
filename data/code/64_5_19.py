def fast_pow(base, exponent, modulus=None):
    if modulus is None:
        return base ** exponent
    else:
        return pow(base, exponent, modulus)

if __name__ == '__main__':
    print(fast_pow(2, 10))
    print(fast_pow(2, 10, 1000))
    print(fast_pow(3, 7, 13))