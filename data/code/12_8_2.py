import math
def simplify_ratio(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    if numerator == 0:
        return 0, 1
    common = math.gcd(abs(numerator), abs(denominator))
    simplified_num = numerator // common
    simplified_den = denominator // common
    if simplified_den < 0:
        simplified_num = -simplified_num
        simplified_den = -simplified_den
    return simplified_num, simplified_den
def calculate_ratio(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b
def find_greatest_common_divisor(a, b):
    return math.gcd(a, b)
def find_least_common_multiple(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // find_greatest_common_divisor(a, b)
def ratio_to_fraction(ratio):
    if ratio == 0:
        return 0, 1
    if ratio == float('inf'):
        return float('inf'), 1
    if ratio == int(ratio):
        return int(ratio), 1
    numerator = int(ratio * 1000000)
    denominator = 1000000
    common, denominator_val = simplify_ratio(numerator, denominator)
    return common, denominator_val
if __name__ == '__main__':
    print("--- Ratio Simplification ---")
    num1, den1 = 12, 18
    s_num, s_den = simplify_ratio(num1, den1)
    print(f"Simplifying {num1}/{den1}: {num1}/{den1} -> {s_num}/{s_den}")
    num2, den2 = 100, 75
    s_num, s_den = simplify_ratio(num2, den2)
    print(f"Simplifying {num2}/{den2}: {num2}/{den2} -> {s_num}/{s_den}")
    print("\n--- Ratio Calculation ---")
    a, b = 20, 5
    ratio = calculate_ratio(a, b)
    print(f"Calculating {a}/{b}: {a}/{b} = {ratio}")
    a, b = 10, 3
    ratio = calculate_ratio(a, b)
    print(f"Calculating {a}/{b}: {a}/{b} = {ratio}")
    print("\n--- GCD and LCM ---")
    x, y = 48, 18
    gcd_val = find_greatest_common_divisor(x, y)
    lcm_val = find_least_common_multiple(x, y)
    print(f"GCD of {x} and {y}: {gcd_val}")
    print(f"LCM of {x} and {y}: {lcm_val}")
    print("\n--- Ratio to Fraction Conversion (Example) ---")
    ratio_val = 1.5
    num_frac, den_frac = ratio_to_fraction(ratio_val)
    print(f"Converting {ratio_val} to fraction (scaled by 1,000,000): {num_frac}/{den_frac}")
    ratio_val = 2.0
    num_frac, den_frac = ratio_to_fraction(ratio_val)
    print(f"Converting {ratio_val} to fraction (scaled by 1,000,000): {num_frac}/{den_frac}")