def fast_power(base, exponent, modulus):
    return pow(base, exponent, modulus)

if __name__ == '__main__':
    result = fast_power(2, 10, 1000)
    print(result)
    result = fast_power(3, 5, 13)
    print(result)
    result = fast_power(5, 0, 7)
    print(result)
    result = fast_power(7, 100, 997)
    print(result)