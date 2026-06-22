from fractions import Fraction

def simplify_ratios(ratio_dict):
    simplified_dict = {}
    for name, ratio in ratio_dict.items():
        numerator, denominator = map(int, ratio.split(':'))
        simplified_ratio = Fraction(numerator, denominator)
        simplified_dict[name] = f"{simplified_ratio.numerator}:{simplified_ratio.denominator}"
    return simplified_dict

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': '4:8',
        'ratio2': '10:25',
        'ratio3': '7:21'
    }
    print(simplify_ratios(sample_ratios))