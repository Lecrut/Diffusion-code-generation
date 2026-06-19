from fractions import Fraction

def simplify_ratios(weight_ratios):
    simplified_ratios = []
    for ratio in weight_ratios:
        numerator, denominator = map(int, ratio.split(':'))
        gcd = Fraction(numerator, denominator).denominator
        simplified_numerator = numerator // gcd
        simplified_denominator = denominator // gcd
        simplified_ratios.append(f"{simplified_numerator}:{simplified_denominator}")
    return simplified_ratios

if __name__ == '__main__':
    sample_values = ['4:6', '10:20', '8:12', '7:3']
    print(simplify_ratios(sample_values))