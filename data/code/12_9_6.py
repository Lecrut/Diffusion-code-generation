import math
def simplify_ratios(ratios):
    simplified = {}
    for name, ratio in ratios.items():
        if ratio == 0:
            simplified[name] = "0"
            continue
        if ratio == 1:
            simplified[name] = "1"
            continue
        common_divisor = math.gcd(int(ratio), int(ratio))
        if common_divisor > 0:
            simplified[name] = str(int(ratio) // common_divisor)
        else:
            simplified[name] = str(ratio)
    return simplified
if __name__ == '__main__':
    sample_ratios = {
        "Red": 2,
        "Green": 4,
        "Blue": 6,
        "Yellow": 8,
        "Purple": 10,
        "Orange": 12
    }
    simplified_ratios = simplify_ratios(sample_ratios)
    print(simplified_ratios)