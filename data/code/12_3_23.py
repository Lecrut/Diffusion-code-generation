from fractions import Fraction

def simplify_ratios(weight_ratios):
    simplified_ratios = []
    for ratio in weight_ratios:
        numerator, denominator = map(int, ratio.split(':'))
        simplified_fraction = Fraction(numerator, denominator)
        simplified_ratio = f"{simplified_fraction.numerator}:{simplified_fraction.denominator}"
        simplified_ratios.append(simplified_ratio)
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = ['4:8', '10:25', '7:3', '9:27']
    print(simplify_ratios(sample_ratios))