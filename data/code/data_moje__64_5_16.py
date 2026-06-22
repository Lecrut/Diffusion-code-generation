def modular_exponentiation(base, power):
    result = pow(base, power, 10**9 + 7)
    return result

if __name__ == '__main__':
    print(modular_exponentiation(2, 10))
    print(modular_exponentiation(3, 5))
    print(modular_exponentiation(10, 2))