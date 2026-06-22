from fractions import Fraction

def simplify_ratios(ratio_dict):
    simplified_dict = {name: Fraction(weight).limit_denominator() for name, weight in ratio_dict.items()}
    return simplified_dict

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': 0.5,
        'ratio2': 0.75,
        'ratio3': 0.8,
        'ratio4': 0.6666666666666666
    }
    
    simplified_ratios = simplify_ratios(sample_ratios)
    print(simplified_ratios)