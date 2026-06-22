def power(base, exponent, modulus=None):
    if modulus is None:
        return base ** exponent
    else:
        return pow(base, exponent, modulus)

if __name__ == '__main__':
    result = power(2, 10)
    print(result)
    result_mod = power(2, 10, 1000)
    print(result_mod)
    result_large_mod = power(5, 100, 13)
    print(result_large_mod)