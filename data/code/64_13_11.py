def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

if __name__ == '__main__':
    large_base = 123456789
    large_exponent = 987654321
    large_modulus = 1000000007
    computed_value = modular_pow(large_base, large_exponent, large_modulus)
    print(computed_value)