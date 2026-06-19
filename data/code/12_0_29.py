from math import gcd

def simplify_ratio(ratio1, ratio2):

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    common_denominator = lcm(ratio1[1], ratio2[1])
    new_ratio1 = (ratio1[0] * (common_denominator // ratio1[1]), common_denominator)
    new_ratio2 = (ratio2[0] * (common_denominator // ratio2[1]), common_denominator)
    total_numerator = new_ratio1[0] + new_ratio2[0]
    common_divisor = gcd(total_numerator, common_denominator)
    simplified_numerator = total_numerator // common_divisor
    simplified_denominator = common_denominator // common_divisor
    return (simplified_numerator, simplified_denominator)
if __name__ == '__main__':
    ratio1 = (3, 4)
    ratio2 = (5, 6)
    result = simplify_ratio(ratio1, ratio2)
    print(result)