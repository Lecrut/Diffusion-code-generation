from math import gcd

def simplify_ratio(ratio1, ratio2):

    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    weight1 = ratio1[0] * ratio2[1]
    weight2 = ratio2[0] * ratio1[1]
    common_divisor = gcd(weight1, weight2)
    simplified_weight1 = weight1 // common_divisor
    simplified_weight2 = weight2 // common_divisor
    return (simplified_weight1, simplified_weight2)
if __name__ == '__main__':
    ratio1 = (3, 4)
    ratio2 = (6, 8)
    result = simplify_ratio(ratio1, ratio2)
    print(result)