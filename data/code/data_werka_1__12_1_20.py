def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_ratio(ratio1, ratio2):
    common_divisor = gcd(ratio1, ratio2)
    simplified_ratio = (ratio1 // common_divisor, ratio2 // common_divisor)
    return simplified_ratio

if __name__ == '__main__':
    ratio1 = 8
    ratio2 = 12
    print(simplify_ratio(ratio1, ratio2))