import math
def simplify_ratio(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return 1 if b != 0 else 0
    if b == 0:
        return 1
    common_divisor = math.gcd(a, b)
    return a // common_divisor, b // common_divisor
if __name__ == '__main__':
    ratio1_a = 12
    ratio1_b = 18
    simplified1 = simplify_ratio(ratio1_a, ratio1_b)
    print(f"Ratio ({ratio1_a}, {ratio1_b}): {simplified1}")
    ratio2_a = 10
    ratio2_b = 25
    simplified2 = simplify_ratio(ratio2_a, ratio2_b)
    print(f"Ratio ({ratio2_a}, {ratio2_b}): {simplified2}")
    ratio3_a = 0
    ratio3_b = 5
    simplified3 = simplify_ratio(ratio3_a, ratio3_b)
    print(f"Ratio ({ratio3_a}, {ratio3_b}): {simplified3}")
    ratio4_a = 0
    ratio4_b = 0
    simplified4 = simplify_ratio(ratio4_a, ratio4_b)
    print(f"Ratio ({ratio4_a}, {ratio4_b}): {simplified4}")
    ratio5_a = 7
    ratio5_b = 7
    simplified5 = simplify_ratio(ratio5_a, ratio5_b)
    print(f"Ratio ({ratio5_a}, {ratio5_b}): {simplified5}")