from math import gcd

def simplify_ratios(weight_ratios):
    def simplify_ratio(ratio):
        numerator, denominator = map(int, ratio.split(':'))
        common_divisor = gcd(numerator, denominator)
        return f"{numerator // common_divisor}:{denominator // common_divisor}"

    return [simplify_ratio(ratio) for ratio in weight_ratios]

if __name__ == '__main__':
    sample_ratios = ["10:20", "35:40", "100:25"]
    print(simplify_ratios(sample_ratios))