def modular_exponentiation(base, exponent, modulus=None):
    if modulus is None:
        modulus = 10**18 + 9
    if exponent < 0:
        raise ValueError("Negative exponents not supported without modular inverse")
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

if __name__ == "__main__":
    base = 2
    exponent = 100
    modulus = 1000000007
    print(modular_exponentiation(base, exponent, modulus))
    print(modular_exponentiation(3, 20, 100))
    print(modular_exponentiation(123456789, 987654321, 10**9 + 7))