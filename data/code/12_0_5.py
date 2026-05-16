import math
def simplify_ratio(ratio1, ratio2):
    if not ratio1 or not ratio2:
        return None
    num1, den1 = ratio1
    num2, den2 = ratio2
    if den1 == 0 or den2 == 0:
        return None
    gcd = math.gcd(num1, num2)
    simplified_num1 = num1 // gcd
    simplified_num2 = num2 // gcd
    return (simplified_num1, simplified_num2)
if __name__ == '__main__':
    ratio_a = (12, 18)
    ratio_b = (24, 36)
    simplified = simplify_ratio(ratio_a, ratio_b)
    if simplified:
        print(simplified)