def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_ratio(ratio1, ratio2):
    common_divisor = gcd(ratio1, ratio2)
    simplified_ratio1 = ratio1 // common_divisor
    simplified_ratio2 = ratio2 // common_divisor
    return (simplified_ratio1, simplified_ratio2)

if __name__ == '__main__':
    ratio1 = 48
    ratio2 = 180
    print(simplify_ratio(ratio1, ratio2))