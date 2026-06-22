import sys

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
    large_base = 723489123487123489123
    large_exponent = 987654321098765432109
    large_modulus = 1000000007
    calculated_result = modular_exponentiation(large_base, large_exponent, large_modulus)
    print(calculated_result)