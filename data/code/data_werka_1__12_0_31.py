from math import gcd

def simplify_ratio(ratio):
    a, b = ratio
    common_divisor = gcd(a, b)
    return (a // common_divisor, b // common_divisor)
if __name__ == '__main__':
    ratio1 = (48, 60)
    ratio2 = (72, 96)
    simplified_ratio1 = simplify_ratio(ratio1)
    simplified_ratio2 = simplify_ratio(ratio2)
    print(simplified_ratio1)
    print(simplified_ratio2)