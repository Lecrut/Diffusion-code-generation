import math
def simplify_ratio(ratio1, ratio2):
    common = math.gcd(ratio1, ratio2)
    simplified_ratio1 = ratio1 // common
    simplified_ratio2 = ratio2 // common
    return (simplified_ratio1, simplified_ratio2)
if __name__ == '__main__':
    ratio_a = 12
    ratio_b = 18
    result_a = simplify_ratio(ratio_a, ratio_b)
    print(f"Simplifying ({ratio_a}, {ratio_b}): {result_a}")
    ratio_c = 100
    ratio_d = 75
    result_c = simplify_ratio(ratio_c, ratio_d)
    print(f"Simplifying ({ratio_c}, {ratio_d}): {result_c}")
    ratio_e = 30
    ratio_f = 42
    result_e = simplify_ratio(ratio_e, ratio_f)
    print(f"Simplifying ({ratio_e}, {ratio_f}): {result_e}")
    ratio_g = 17
    ratio_h = 5
    result_g = simplify_ratio(ratio_g, ratio_h)
    print(f"Simplifying ({ratio_g}, {ratio_h}): {result_g}")