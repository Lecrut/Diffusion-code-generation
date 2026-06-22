def binary_exponentiation(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        base = 1 / base
        exp = -exp
    result = 1
    current_base = base
    current_exp = exp
    while current_exp > 0:
        if current_exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        current_exp //= 2
    return result

if __name__ == '__main__':
    base = 2
    exp = 10
    print(binary_exponentiation(base, exp))