import math
def simplify_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    if numerator == 0:
        return 0, 1
    common_divisor = math.gcd(abs(numerator), abs(denominator))
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    if simplified_denominator < 0:
        simplified_numerator = -simplified_numerator
        simplified_denominator = -simplified_denominator
    return simplified_numerator, simplified_denominator
def calculate_ratio(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b
def find_greatest_common_divisor(a, b):
    return math.gcd(a, b)
def reduce_to_simplest_fraction(num, den):
    if den == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if num == 0:
        return 0, 1
    common = find_greatest_common_divisor(abs(num), abs(den))
    new_num = num // common
    new_den = den // common
    if new_den < 0:
        new_num = -new_num
        new_den = -new_den
    return new_num, new_den
if __name__ == '__main__':
    print("--- Ratio Simplification Tests ---")
    num1, den1 = 12, 18
    s_num1, s_den1 = simplify_ratio(num1, den1)
    print(f"Ratio {num1}/{den1}: Simplified to {s_num1}/{s_den1}")
    num2, den2 = 100, 25
    s_num2, s_den2 = simplify_ratio(num2, den2)
    print(f"Ratio {num2}/{den2}: Simplified to {s_num2}/{s_den2}")
    num3, den3 = -20, 40
    s_num3, s_den3 = simplify_ratio(num3, den3)
    print(f"Ratio {num3}/{den3}: Simplified to {s_num3}/{s_den3}")
    num4, den4 = 7, 11
    s_num4, s_den4 = simplify_ratio(num4, den4)
    print(f"Ratio {num4}/{den4}: Simplified to {s_num4}/{s_den4}")
    print("\n--- Ratio Calculation Tests ---")
    a = 15
    b = 5
    ratio = calculate_ratio(a, b)
    print(f"Ratio {a}/{b}: {ratio}")
    a = 10
    b = 3
    ratio = calculate_ratio(a, b)
    print(f"Ratio {a}/{b}: {ratio}")
    print("\n--- GCD Tests ---")
    x = 48
    y = 18
    gcd_val = find_greatest_common_divisor(x, y)
    print(f"GCD of {x} and {y}: {gcd_val}")
    x = -30
    y = 45
    gcd_val = find_greatest_common_divisor(x, y)
    print(f"GCD of {x} and {y}: {gcd_val}")
    print("\n--- Reduction Tests ---")
    n = 36
    d = 12
    r_n, r_d = reduce_to_simplest_fraction(n, d)
    print(f"Reduce {n}/{d}: {r_n}/{r_d}")
    n = -50
    d = 25
    r_n, r_d = reduce_to_simplest_fraction(n, d)
    print(f"Reduce {n}/{d}: {r_n}/{r_d}")