from fractions import Fraction

def simplify_ratios(ratios):
    simplified_ratios = []
    for ratio in ratios:
        numerator, denominator = map(int, ratio.split(':'))
        simplified_fraction = Fraction(numerator, denominator)
        simplified_ratios.append(f"{simplified_fraction.numerator}:{simplified_fraction.denominator}")
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = ['4:6', '10:20', '8:12', '7:3']
    print(simplify_ratios(sample_ratios))