import math
def simplify_ratio(ratio):
    if ratio == 0:
        return (0, 0)
    common = math.gcd(ratio[0], ratio[1])
    return (ratio[0] // common, ratio[1] // common)
def simplify_ratios(ratios):
    simplified = []
    for ratio in ratios:
        simplified.append(simplify_ratio(ratio))
    return simplified
if __name__ == '__main__':
    sample_ratios = [
        (10, 20),
        (6, 9),
        (15, 25),
        (7, 14),
        (100, 50),
        (12, 18)
    ]
    result = simplify_ratios(sample_ratios)
    print(result)