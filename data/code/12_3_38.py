from math import gcd

def simplify_ratios(weight_ratios):
    simplified_ratios = []
    for ratio in weight_ratios:
        if len(ratio) != 2 or not all(isinstance(x, int) and x > 0 for x in ratio):
            raise ValueError("Each ratio must be a tuple of two positive integers.")
        common_divisor = gcd(ratio[0], ratio[1])
        simplified_ratio = (ratio[0] // common_divisor, ratio[1] // common_divisor)
        simplified_ratios.append(simplified_ratio)
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = [(4, 8), (10, 5), (7, 3), (20, 10)]
    print(simplify_ratios(sample_ratios))