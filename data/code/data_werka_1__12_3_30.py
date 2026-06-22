from fractions import Fraction

def simplify_ratios(weight_ratios):
    simplified_ratios = []
    for ratio in weight_ratios:
        fraction = Fraction(ratio).limit_denominator()
        simplified_ratios.append((fraction.numerator, fraction.denominator))
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = [0.5, 0.75, 1.25, 2.5, 3.75]
    print(simplify_ratios(sample_ratios))