def optimized_pow(base, exp):
    if not isinstance(base, (int, float)) or not isinstance(exp, (int, float)):
        raise TypeError("Base and exponent must be numeric")
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0:
        return 1 / optimized_pow(base, -exp)
    result = 1
    current_base = base
    current_exp = int(exp) if exp == int(exp) else exp
    if isinstance(current_exp, float):
        return base ** exp
    while current_exp > 0:
        if current_exp % 2 == 1:
            result *= current_base
        current_base *= current_base
        current_exp //= 2
    return result

if __name__ == '__main__':
    print(optimized_pow(2, 10))
    print(optimized_pow(3, 5))
    print(optimized_pow(2, -3))
    print(optimized_pow(5.5, 3))
    print(optimized_pow(10, 0))
    print(optimized_pow(2, 20))