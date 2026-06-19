from math import gcd

def simplify_ratio(ratio1, ratio2):
    num1, denom1 = ratio1
    num2, denom2 = ratio2
    
    total_num = num1 + num2
    total_denom = denom1 + denom2
    
    common_divisor = gcd(total_num, total_denom)
    
    simplified_num = total_num // common_divisor
    simplified_denom = total_denom // common_divisor
    
    return (simplified_num, simplified_denom)

if __name__ == '__main__':
    ratio1 = (3, 4)
    ratio2 = (5, 6)
    
    result = simplify_ratio(ratio1, ratio2)
    print(result)