def modular_power(base, exponent, modulus):
    if modulus == 1:
        return 0
    return pow(base, exponent, modulus)

if __name__ == '__main__':
    base_val = 2
    exponent_val = 10
    modulus_val = 1000
    result = modular_power(base_val, exponent_val, modulus_val)
    print(result)