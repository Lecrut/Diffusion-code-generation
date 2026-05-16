import math
def simplify_ratios(ratios):
    simplified = {}
    for name, ratio in ratios.items():
        if ratio == 0:
            simplified[name] = "0"
            continue
        if isinstance(ratio, (int, float)):
            if ratio == 0:
                simplified[name] = "0"
            else:
                common = math.gcd(int(ratio) if ratio == int(ratio) else int(ratio), int(ratio))
                simplified[name] = f"{int(ratio) // common}/{int(ratio) // common}"
        else:
            simplified[name] = ratio
    return simplified
if __name__ == '__main__':
    sample_ratios = {
        "A:B": 2,
        "C:D": 6,
        "E:F": 10,
        "G:H": 15,
        "I:J": 4,
        "K:L": 8
    }
    simplified_ratios = simplify_ratios(sample_ratios)
    print(simplified_ratios)