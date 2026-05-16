import math
def simplify_ratio(ratio):
    if ratio == 0:
        return (0, 0)
    common = math.gcd(ratio[0], ratio[1])
    return (ratio[0] // common, ratio[1] // common)
def simplify_weight_ratios(ratios):
    simplified_ratios = []
    for ratio in ratios:
        simplified = simplify_ratio(ratio)
        simplified_ratios.append(simplified)
    return simplified_ratios
if __name__ == '__main__':
    sample_ratios = [
        (10, 20),
        (12, 18),
        (7, 14),
        (15, 25),
        (100, 50),
        (0, 5)
    ]
    result = simplify_weight_ratios(sample_ratios)
    print(result)