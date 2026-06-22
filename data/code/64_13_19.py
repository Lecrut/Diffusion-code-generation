def mod_pow(base, exponent, modulus=None):
    if modulus is None:
        result = 1
        base = base % 1 if base < 0 else base
        while exponent > 0:
            if exponent % 2 == 1:
                result = result * base
            exponent = exponent // 2
            if exponent > 0:
                base = base * base
        return result
    else:
        if modulus == 1:
            return 0
        result = 1
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent // 2
            if exponent > 0:
                base = (base * base) % modulus
        return result

if __name__ == '__main__':
    print(mod_pow(2, 10))
    print(mod_pow(3, 5, 7))
    print(mod_pow(123456789, 987654321, 1000000007))
    print(mod_pow(0, 100))
    print(mod_pow(10, 10, 1))
    print(mod_pow(2, 0, 5))