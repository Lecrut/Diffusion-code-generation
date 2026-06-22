import sys

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

def power_without_mod(base, exponent):
    if exponent < 0:
        return 0
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base
        exponent = exponent >> 1
        base = base * base
    return result

if __name__ == '__main__':
    large_base = 2
    large_exponent = 1000
    large_modulus = 10**9 + 7
    computed_modular = modular_exponentiation(large_base, large_exponent, large_modulus)
    small_base = 3
    small_exponent = 4
    computed_power = power_without_mod(small_base, small_exponent)
    print(computed_modular)
    print(computed_power)