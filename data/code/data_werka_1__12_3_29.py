from math import gcd
from functools import reduce

def simplify_ratios(ratios):
    def simplify_ratio(ratio):
        num, denom = ratio
        common_divisor = gcd(num, denom)
        return (num // common_divisor, denom // common_divisor)

    return [simplify_ratio(ratio) for ratio in ratios]

if __name__ == '__main__':
    sample_ratios = [(4, 8), (10, 5), (7, 3), (20, 100)]
    simplified_ratios = simplify_ratios(sample_ratios)
    print(simplified_ratios)