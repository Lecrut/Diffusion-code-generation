import math

def simplify_ratio(numerator, denominator):
    common_divisor = math.gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

if __name__ == '__main__':
    ratio1_num, ratio1_den = 6, 9
    factor1 = 2
    scaled_ratio1 = simplify_ratio(ratio1_num * factor1, ratio1_den * factor1)
    print(f"Ratio: {ratio1_num}:{ratio1_den}, Factor: {factor1}, Result: {scaled_ratio1[0]}:{scaled_ratio1[1]}")

    ratio2_num, ratio2_den = 10, 15
    factor2 = 4
    scaled_ratio2 = simplify_ratio(ratio2_num * factor2, ratio2_den * factor2)
    print(f"Ratio: {ratio2_num}:{ratio2_den}, Factor: {factor2}, Result: {scaled_ratio2[0]}:{scaled_ratio2[1]}")