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
    print(modular_power(2, 10, 1000))
    print(modular_power(3, 3, 7))
    print(modular_power(5, 0, 11))
    print(modular_power(7, 2, 1))