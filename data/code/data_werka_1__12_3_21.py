from math import gcd

def simplify_ratios(weight_ratios):
    simplified = []
    for ratio in weight_ratios:
        numerator, denominator = map(int, ratio.split(':'))
        common_divisor = gcd(numerator, denominator)
        simplified_ratio = f"{numerator // common_divisor}:{denominator // common_divisor}"
        simplified.append(simplified_ratio)
    return simplified

if __name__ == '__main__':
    sample_ratios = ["10:20", "35:40", "100:25"]
    print(simplify_ratios(sample_ratios))