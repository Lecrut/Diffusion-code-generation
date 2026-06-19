from math import gcd

def simplify_ratios(ratio_dict):
    simplified_ratios = {}
    for name, ratio in ratio_dict.items():
        num, denom = map(int, ratio.split(':'))
        common_divisor = gcd(num, denom)
        simplified_num = num // common_divisor
        simplified_denom = denom // common_divisor
        simplified_ratios[name] = f"{simplified_num}:{simplified_denom}"
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': '4:8',
        'ratio2': '10:25',
        'ratio3': '7:9'
    }
    print(simplify_ratios(sample_ratios))