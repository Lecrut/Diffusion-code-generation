def modular_exponentiation(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

if __name__ == '__main__':
    sample_base = 7
    sample_exponent = 123456789
    sample_modulus = 1000000007
    computed_value = modular_exponentiation(sample_base, sample_exponent, sample_modulus)
    print(computed_value)