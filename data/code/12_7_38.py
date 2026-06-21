from math import gcd

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return f"{numerator // common_divisor}:{denominator // common_divisor}"

def simplify_ratios(ratio_dict):
    simplified_dict = {}
    for name, ratio in ratio_dict.items():
        num, denom = map(int, ratio.split(':'))
        simplified_dict[name] = simplify_ratio(num, denom)
    return simplified_dict

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': '6:9',
        'ratio2': '15:20',
        'ratio3': '8:12'
    }
    print(simplify_ratios(sample_ratios))