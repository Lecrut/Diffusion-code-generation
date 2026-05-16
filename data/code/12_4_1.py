import math
def simplify_ratio(ratio):
    if ratio == 0:
        return (0, 0)
    common = math.gcd(ratio[0], ratio[1])
    return (ratio[0] // common, ratio[1] // common)
def simplify_ratios(weight_ratios):
    simplified_list = []
    for ratio in weight_ratios:
        simplified_list.append(simplify_ratio(ratio))
    return simplified_list
if __name__ == '__main__':
    sample_ratios = [
        (10, 20),
        (12, 18),
        (7, 14),
        (15, 25),
        (100, 50)
    ]
    result = simplify_ratios(sample_ratios)
    print(result)