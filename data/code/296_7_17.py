def simplify_ratio(numerator, denominator):
    gcd = numerator
    while denominator % gcd != 0:
        gcd -= 1
    return (numerator // gcd, denominator // gcd)

def are_in_proportion(a, b, c, d):
    return simplify_ratio(a, b) == simplify_ratio(c, d)

if __name__ == '__main__':
    a_val = 8
    b_val = 4
    c_val = 16
    d_val = 8
    if are_in_proportion(a_val, b_val, c_val, d_val):
        print(f"{a_val}:{b_val} is in proportion with {c_val}:{d_val}")
        simplified_ratio = simplify_ratio(a_val, b_val)
        print(f"Simplified ratio: {simplified_ratio[0]}:{simplified_ratio[1]}")
    else:
        print(f"{a_val}:{b_val} is not in proportion with {c_val}:{d_val}")