def validate_exponent(base, exponent):
    if not isinstance(exponent, int) or exponent < 0:
        raise ValueError("Exponent must be a non-negative integer")

def binary_exponentiation(base, exponent):
    validate_exponent(base, exponent)
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

if __name__ == '__main__':
    print(binary_exponentiation(2, 10))