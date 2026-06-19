from math import gcd

def simplify_ratio(ratio):
    numerator = ratio[0]
    denominator = ratio[1]
    common_divisor = gcd(numerator, denominator)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    ratio1 = (8, 12)
    ratio2 = (20, 15)
    
    simplified_ratio1 = simplify_ratio(ratio1)
    simplified_ratio2 = simplify_ratio(ratio2)
    
    print(simplified_ratio1)
    print(simplified_ratio2)