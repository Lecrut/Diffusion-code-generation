from math import gcd
from functools import reduce

def simplify_ratios(weight_ratios):
    def lcm(a, b):
        return abs(a*b) // gcd(a, b)
    
    def lcm_list(lst):
        return reduce(lcm, lst)
    
    simplified_ratios = []
    for ratio in weight_ratios:
        common_divisor = gcd(*ratio)
        simplified_ratio = tuple(x // common_divisor for x in ratio)
        lcm_value = lcm_list(simplified_ratio)
        normalized_ratio = tuple(x * (lcm_value // y) for x, y in zip(ratio, simplified_ratio))
        simplified_ratios.append(normalized_ratio)
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = [(4, 6), (8, 12), (10, 15)]
    print(simplify_ratios(sample_ratios))