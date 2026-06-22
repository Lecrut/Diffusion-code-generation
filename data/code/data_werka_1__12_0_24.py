from math import gcd

def simplify_ratio(ratio1, ratio2):
    num1, den1 = ratio1
    num2, den2 = ratio2
    common_divisor = gcd(gcd(num1, den1), gcd(num2, den2))
    simplified_ratio1 = (num1 // common_divisor, den1 // common_divisor)
    simplified_ratio2 = (num2 // common_divisor, den2 // common_divisor)
    return (simplified_ratio1, simplified_ratio2)
if __name__ == '__main__':
    ratio1 = (4, 8)
    ratio2 = (6, 12)
    simplified_ratios = simplify_ratio(ratio1, ratio2)
    print(simplified_ratios)