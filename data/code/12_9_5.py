import math
def simplify_ratios(ratios):
    simplified = {}
    for name, ratio in ratios.items():
        if ratio == 0:
            simplified[name] = "0"
        else:
            common_divisor = math.gcd(int(ratio), int(ratio))
            simplified[name] = ratio / common_divisor
    return simplified
if __name__ == '__main__':
    sample_ratios = {
        "A:B": 10,
        "C:D": 15,
        "E:F": 20,
        "G:H": 4,
        "I:J": 100
    }
    simplified_ratios = simplify_ratios(sample_ratios)
    print(simplified_ratios)