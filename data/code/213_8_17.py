def binary_exponentiation(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

if __name__ == '__main__':
    base_value = 5
    exponent_value = 8
    print(binary_exponentiation(base_value, exponent_value))