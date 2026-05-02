import math
def simplify_ratio(ratio):
    if ratio == 0:
        return (0, 0)
    common_divisor = math.gcd(int(ratio), int(ratio))
    return (int(ratio) // common_divisor, int(ratio) // common_divisor)
def simplify_weight_ratios(ratios):
    simplified_ratios = []
    for ratio in ratios:
        if isinstance(ratio, (int, float)):
            if ratio == 0:
                simplified_ratios.append((0, 0))
            else:
                num = int(ratio)
                den = int(ratio)
                if num == 0 or den == 0:
                    simplified_ratios.append((num, den))
                else:
                    common = math.gcd(num, den)
                    simplified_ratios.append((num // common, den // common))
        else:
            simplified_ratios.append(ratio)
    return simplified_ratios
if __name__ == '__main__':
    sample_ratios = [2, 4, 6, 8, 10, 12, 15, 16.0, 0.0, 7]
    simplified = simplify_weight_ratios(sample_ratios)
    print(simplified)