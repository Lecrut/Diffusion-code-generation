from math import gcd

def simplify_ratio(ratio1, ratio2):
    common_divisor = gcd(ratio1, ratio2)
    simplified_ratio = (ratio1 // common_divisor, ratio2 // common_divisor)
    return simplified_ratio

if __name__ == '__main__':
    ratio1 = 48
    ratio2 = 64
    print(simplify_ratio(ratio1, ratio2))