def binary_exponentiation(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        exponent //= 2
        base *= base
    return result

if __name__ == '__main__':
    print(binary_exponentiation(2, 15))