import math
def simplify_ratio(ratio1, ratio2):
    if not ratio1 or not ratio2:
        return None
    num1, den1 = ratio1
    num2, den2 = ratio2
    gcd1 = math.gcd(num1, den1)
    gcd2 = math.gcd(num2, den2)
    gcd = math.gcd(gcd1, gcd2)
    simplified_num1 = num1 // gcd
    simplified_den1 = den1 // gcd
    simplified_num2 = num2 // gcd
    simplified_den2 = den2 // gcd
    return (simplified_num1, simplified_den1), (simplified_num2, simplified_den2)
if __name__ == '__main__':
    ratio_a = (12, 18)
    ratio_b = (20, 30)
    result_a, result_b = simplify_ratio(ratio_a, ratio_b)
    print(f"Ratio A: {ratio_a}")
    print(f"Ratio B: {ratio_b}")
    print(f"Simplified Ratio A: {result_a}")
    print(f"Simplified Ratio B: {result_b}")