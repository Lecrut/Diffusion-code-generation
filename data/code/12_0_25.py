from math import gcd

def simplify_ratio(ratio1, ratio2):

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    num1, denom1 = ratio1
    num2, denom2 = ratio2
    common_denom = lcm(denom1, denom2)
    scaled_num1 = num1 * (common_denom // denom1)
    scaled_num2 = num2 * (common_denom // denom2)
    total_num = scaled_num1 + scaled_num2
    total_gcd = gcd(total_num, common_denom)
    simplified_numerator = total_num // total_gcd
    simplified_denominator = common_denom // total_gcd
    return (simplified_numerator, simplified_denominator)
if __name__ == '__main__':
    ratio1 = (3, 4)
    ratio2 = (5, 6)
    result = simplify_ratio(ratio1, ratio2)
    print(result)