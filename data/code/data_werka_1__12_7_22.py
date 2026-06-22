from math import gcd

def simplify_ratios(ratio_dict):
    simplified_dict = {}
    for name, (numerator, denominator) in ratio_dict.items():
        common_divisor = gcd(numerator, denominator)
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor
        simplified_dict[name] = (simplified_numerator, simplified_denominator)
    return simplified_dict

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': (4, 8),
        'ratio2': (10, 5),
        'ratio3': (7, 3)
    }
    print(simplify_ratios(sample_ratios))