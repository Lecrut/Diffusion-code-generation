from math import gcd
from functools import reduce

def simplify_ratios(ratio_dict):
    def simplify_ratio(numerator, denominator):
        common_divisor = gcd(numerator, denominator)
        return (numerator // common_divisor, denominator // common_divisor)

    simplified_dict = {}
    for name, ratio in ratio_dict.items():
        numerator, denominator = map(int, ratio.split(':'))
        simplified_numerator, simplified_denominator = simplify_ratio(numerator, denominator)
        simplified_dict[name] = f"{simplified_numerator}:{simplified_denominator}"
    
    return simplified_dict

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': '4:8',
        'ratio2': '10:5',
        'ratio3': '7:21'
    }
    
    simplified_ratios = simplify_ratios(sample_ratios)
    print(simplified_ratios)