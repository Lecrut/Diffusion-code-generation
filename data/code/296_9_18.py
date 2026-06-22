def add_ratios(ratio1, ratio2):
    numerator = ratio1[0] * ratio2[1] + ratio1[1] * ratio2[0]
    denominator = ratio1[1] * ratio2[1]
    return simplify_ratio(numerator, denominator)

def simplify_ratio(numerator, denominator):
    gcd = get_gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)

def get_gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a
if __name__ == '__main__':
    ratio1 = (3, 4)
    ratio2 = (5, 6)
    result = add_ratios(ratio1, ratio2)
    print(result)