def modular_exponentiation(base, exponent, modulus):
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
    large_base = 12345678901234567890
    large_exponent = 9876543210987654321
    large_modulus = 1000000007
    computed_value = modular_exponentiation(large_base, large_exponent, large_modulus)
    print(computed_value)