from math import gcd

def simplify_ratios(ratio_dict):
    simplified_dict = {}
    for name, ratio in ratio_dict.items():
        num, denom = map(int, ratio.split(':'))
        common_divisor = gcd(num, denom)
        simplified_ratio = f"{num // common_divisor}:{denom // common_divisor}"
        simplified_dict[name] = simplified_ratio
    return simplified_dict

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': '4:8',
        'ratio2': '10:25',
        'ratio3': '7:14'
    }
    print(simplify_ratios(sample_ratios))