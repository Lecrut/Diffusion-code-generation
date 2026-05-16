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
        "1:2": 4,
        "3:4": 12,
        "5:10": 20,
        "7:14": 28,
        "2:4": 8,
        "1:3": 3,
        "6:9": 18
    }
    simplified_ratios = simplify_ratios(sample_ratios)
    print(simplified_ratios)