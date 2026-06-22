import time

def modular_power(base, exponent, modulus):
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
    large_base = 123456789012345678901234567890
    large_exponent = 1234567890123456789012345678901234567890
    large_modulus = 1000000007
    start_time = time.time()
    computed_value = modular_power(large_base, large_exponent, large_modulus)
    end_time = time.time()
    print(computed_value)
    print(end_time - start_time)