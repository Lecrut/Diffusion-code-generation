import math
def simplify_ratio(numerator, denominator):
    common = math.gcd(numerator, denominator)
    return numerator // common, denominator // common
def calculate_and_simplify_ratio(ratio_a_b, ratio_c_d):
    a, b = ratio_a_b
    c, d = ratio_c_d
    numerator = a * d
    denominator = b * c
    return simplify_ratio(numerator, denominator)
if __name__ == '__main__':
    ratio1 = (2, 3)
    ratio2 = (4, 5)
    result = calculate_and_simplify_ratio(ratio1, ratio2)
    print(f"Ratio 1: {ratio1}")
    print(f"Ratio 2: {ratio2}")
    print(f"Equivalent ratio AD:BC (simplified): {result}")