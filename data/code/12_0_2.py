import math
def simplify_ratio(ratio1, ratio2):
    if not ratio1 or not ratio2:
        return None
    n1 = ratio1[0]
    d1 = ratio1[1]
    n2 = ratio2[0]
    d2 = ratio2[1]
    gcd = math.gcd(n1, n2)
    simplified_n1 = n1 // gcd
    simplified_d1 = d1 // gcd
    simplified_n2 = n2 // gcd
    simplified_d2 = d2 // gcd
    return (simplified_n1, simplified_d1), (simplified_n2, simplified_d2)
if __name__ == '__main__':
    ratio_a = (12, 18)
    ratio_b = (20, 30)
    result_a, result_b = simplify_ratio(ratio_a, ratio_b)
    print(f"Ratio 1: {ratio_a}")
    print(f"Ratio 2: {ratio_b}")
    print(f"Simplified Ratio 1: {result_a}")
    print(f"Simplified Ratio 2: {result_b}")