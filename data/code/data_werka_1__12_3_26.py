from fractions import Fraction

def simplify_ratios(weight_ratios):
    simplified_ratios = [Fraction(ratio).limit_denominator() for ratio in weight_ratios]
    return [f"{simplified_ratio.numerator}:{simplified_ratio.denominator}" for simplified_ratio in simplified_ratios]

if __name__ == '__main__':
    sample_ratios = [0.5, 1.25, 0.75, 2.5, 3.75]
    print(simplify_ratios(sample_ratios))