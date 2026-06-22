def calculate_power(base, exponent, modulus=None):
    if modulus is not None:
        return pow(base, exponent, modulus)
    return base ** exponent

if __name__ == '__main__':
    result = calculate_power(2, 10, 1000)
    print(result)
    result2 = calculate_power(3, 5)
    print(result2)