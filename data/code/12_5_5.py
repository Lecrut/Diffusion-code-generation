import math
def simplify_ratio(numerator, denominator):
    common = math.gcd(numerator, denominator)
    return numerator // common, denominator // common
def calculate_and_simplify_ratio(ratio1_str, ratio2_str):
    parts1 = ratio1_str.split(':')
    A = int(parts1[0])
    B = int(parts1[1])
    parts2 = ratio2_str.split(':')
    C = int(parts2[0])
    D = int(parts2[1])
    numerator = A * D
    denominator = B * C
    num_simplified, den_simplified = simplify_ratio(numerator, denominator)
    return f"{num_simplified}:{den_simplified}"
if __name__ == '__main__':
    ratio1 = "2:3"
    ratio2 = "4:5"
    result = calculate_and_simplify_ratio(ratio1, ratio2)
    print(result)