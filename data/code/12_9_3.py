import math
def simplify_ratios(ratios):
    simplified = {}
    for name, ratio in ratios.items():
        if ratio == 0:
            simplified[name] = "0"
        else:
            common = math.gcd(ratio)
            simplified[name] = ratio / common
    return simplified
if __name__ == '__main__':
    sample_ratios = {
        "A": 12,
        "B": 18,
        "C": 24,
        "D": 10,
        "E": 30
    }
    result = simplify_ratios(sample_ratios)
    print(result)