from math import gcd

class RatioSimplifier:
    @staticmethod
    def simplify(ratio):
        numerator, denominator = map(int, ratio.split(':'))
        common_divisor = gcd(numerator, denominator)
        return f"{numerator // common_divisor}:{denominator // common_divisor}"

def simplify_ratios(weight_ratios):
    simplifier = RatioSimplifier()
    return [simplifier.simplify(ratio) for ratio in weight_ratios]

if __name__ == '__main__':
    sample_ratios = ["10:25", "8:16", "45:90", "7:3"]
    print(simplify_ratios(sample_ratios))