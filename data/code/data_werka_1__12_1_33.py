from math import gcd

def simplify_ratio(ratio1, ratio2):
    common_divisor = gcd(ratio1, ratio2)
    simplified_ratio1 = ratio1 // common_divisor
    simplified_ratio2 = ratio2 // common_divisor
    return (simplified_ratio1, simplified_ratio2)

if __name__ == '__main__':
    sample_ratio1 = 18
    sample_ratio2 = 24
    result = simplify_ratio(sample_ratio1, sample_ratio2)
    print(result)