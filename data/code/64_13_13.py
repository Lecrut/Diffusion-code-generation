def modular_power(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base % modulus
        exponent = exponent >> 1
        base = base * base % modulus
    return result

def large_integer_power(base, exponent):
    if exponent < 0:
        raise ValueError('Exponent must be non-negative for integer arithmetic')
    if exponent == 0:
        return 1
    return pow(base, exponent)
if __name__ == '__main__':
    base = 2
    exponent = 100
    modulus = 1000000007
    result_modular = modular_power(base, exponent, modulus)
    print(result_modular)
    base_large = 123456789
    exponent_large = 987654321
    result_large = large_integer_power(base_large, exponent_large)
    print(result_large)
    base_test = 3
    exponent_test = 5
    result_simple = large_integer_power(base_test, exponent_test)
    print(result_simple)