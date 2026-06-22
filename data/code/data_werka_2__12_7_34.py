from math import gcd

def simplify_ratios(ratio_dict):
    def parse_ratio(ratio_str):
        return map(int, ratio_str.split(':'))

    simplified_dict = {}
    for name, ratio in ratio_dict.items():
        numerator, denominator = parse_ratio(ratio)
        common_divisor = gcd(numerator, denominator)
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor
        simplified_dict[name] = f"{simplified_numerator}:{simplified_denominator}"
    return simplified_dict

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': '4:8',
        'ratio2': '10:25',
        'ratio3': '7:21'
    }
    print(simplify_ratios(sample_ratios))