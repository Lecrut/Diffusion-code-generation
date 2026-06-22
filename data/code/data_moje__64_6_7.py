def power_by_squaring(base, exp):
    if exp < 0:
        return 1.0 / power_by_squaring(base, -exp)
    result = 1
    current_base = base
    current_exp = exp
    while current_exp > 0:
        if current_exp & 1:
            result *= current_base
        current_base *= current_base
        current_exp >>= 1
    return result

if __name__ == '__main__':
    print(power_by_squaring(2, 10))
    print(power_by_squaring(3, 5))
    print(power_by_squaring(5, 0))
    print(power_by_squaring(2, -3))