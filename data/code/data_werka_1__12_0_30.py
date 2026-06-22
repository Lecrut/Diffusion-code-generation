from math import gcd

def simplify_ratio(ratio):
    a, b = ratio
    common_divisor = gcd(a, b)
    return (a // common_divisor, b // common_divisor)

if __name__ == '__main__':
    weight_ratio1 = (8, 12)
    weight_ratio2 = (10, 15)
    
    simplified_ratio1 = simplify_ratio(weight_ratio1)
    simplified_ratio2 = simplify_ratio(weight_ratio2)
    
    print(simplified_ratio1)
    print(simplified_ratio2)