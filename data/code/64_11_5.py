def power(base, exp):
    if exp < 0:
        return 1 / power(-base, -exp) if base == 0 else 1 / power(base, -exp)
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
    print(power(2, 10))
    print(power(-3, 3))
    print(power(5, 0))
    print(power(-2, 4))
    print(power(0, 5))