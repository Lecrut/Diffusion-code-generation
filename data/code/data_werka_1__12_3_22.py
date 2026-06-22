from math import gcd

def simplify_ratios(weight_ratios):
    simplified_ratios = []
    for ratio in weight_ratios:
        num, denom = map(int, ratio.split(':'))
        common_divisor = gcd(num, denom)
        simplified_num = num // common_divisor
        simplified_denom = denom // common_divisor
        simplified_ratios.append(f"{simplified_num}:{simplified_denom}")
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = ["4:6", "10:20", "8:12", "7:3"]
    print(simplify_ratios(sample_ratios))