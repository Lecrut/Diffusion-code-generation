from fractions import Fraction

def simplify_ratios(weight_ratios):
    simplified_ratios = []
    for ratio in weight_ratios:
        numerator, denominator = map(int, ratio.split(':'))
        fraction = Fraction(numerator, denominator)
        simplified_ratio = f"{fraction.numerator}:{fraction.denominator}"
        simplified_ratios.append(simplified_ratio)
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = ['4:6', '10:20', '7:3', '8:12']
    print(simplify_ratios(sample_ratios))