def modular_exponentiation(base, exponent, modulus):
    return pow(base, exponent, modulus)

if __name__ == '__main__':
    base_value = 2
    exponent_value = 10
    modulus_value = 1000
    result = modular_exponentiation(base_value, exponent_value, modulus_value)
    print(result)