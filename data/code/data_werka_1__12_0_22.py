import math

def simplify_ratio(ratio):
    gcd = math.gcd(*ratio)
    return (ratio[0] // gcd, ratio[1] // gcd)

if __name__ == '__main__':
    weight_ratio_1 = (8, 12)
    weight_ratio_2 = (15, 25)
    
    simplified_ratio_1 = simplify_ratio(weight_ratio_1)
    simplified_ratio_2 = simplify_ratio(weight_ratio_2)
    
    print(simplified_ratio_1)
    print(simplified_ratio_2)