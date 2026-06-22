from fractions import Fraction

def simplify_ratios(weight_ratios):
    simplified_ratios = [Fraction(ratio).limit_denominator() for ratio in weight_ratios]
    return [f"{frac.numerator}/{frac.denominator}" for frac in simplified_ratios]

if __name__ == '__main__':
    sample_ratios = [0.5, 0.75, 1.25, 0.333333, 0.666666]
    simplified = simplify_ratios(sample_ratios)
    print(simplified)