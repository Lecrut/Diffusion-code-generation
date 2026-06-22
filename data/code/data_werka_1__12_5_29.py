import math

def simplify_weight_ratio(weight1, weight2):
    if weight1 == 0 and weight2 == 0:
        return (0, 0)
    gcd = math.gcd(abs(weight1), abs(weight2))
    simplified_weight1 = weight1 // gcd
    simplified_weight2 = weight2 // gcd
    return (simplified_weight1, simplified_weight2)
if __name__ == '__main__':
    weight1 = 100
    weight2 = 200
    result = simplify_weight_ratio(weight1, weight2)
    print(result)