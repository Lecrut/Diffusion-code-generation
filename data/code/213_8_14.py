def binary_exponentiation(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

if __name__ == '__main__':
    BASE_VALUE = 5
    EXPONENT_VALUE = 3
    print(binary_exponentiation(BASE_VALUE, EXPONENT_VALUE))