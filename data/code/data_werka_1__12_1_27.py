def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def simplify_ratio(ratio1, ratio2):
    common_divisor = gcd(ratio1, ratio2)
    simplified_ratio = (ratio1 // common_divisor, ratio2 // common_divisor)
    return simplified_ratio

if __name__ == '__main__':
    sample_ratio1 = 45
    sample_ratio2 = 100
    result = simplify_ratio(sample_ratio1, sample_ratio2)
    print(result)