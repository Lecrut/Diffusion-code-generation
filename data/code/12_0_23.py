from math import gcd

def simplify_ratio(ratio1, ratio2):
    gcd_value = gcd(gcd(ratio1[0], ratio1[1]), gcd(ratio2[0], ratio2[1]))
    simplified_ratio1 = (ratio1[0] // gcd_value, ratio1[1] // gcd_value)
    simplified_ratio2 = (ratio2[0] // gcd_value, ratio2[1] // gcd_value)
    return (simplified_ratio1, simplified_ratio2)
if __name__ == '__main__':
    ratio1 = (48, 64)
    ratio2 = (72, 96)
    simplified_ratios = simplify_ratio(ratio1, ratio2)
    print(simplified_ratios)