def power_with_modulus(base: int, exponent: int, modulus: int = 1) -> int:
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

def power_no_modulus(base: int, exponent: int) -> int:
    if exponent == 0:
        return 1
    if base == 0:
        return 0
    if exponent < 0:
        raise ValueError("Negative exponents not supported for integer arithmetic without modulus")
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        exponent = exponent >> 1
        base *= base
    return result

if __name__ == '__main__':
    val1 = power_with_modulus(2, 10, 1000)
    print(val1)
    val2 = power_no_modulus(3, 10)
    print(val2)
    val3 = power_with_modulus(2, 10, 1)
    print(val3)