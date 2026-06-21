from math import gcd

def parse_ratio(ratio_str):
    try:
        num, denom = map(int, ratio_str.split(':'))
        if denom == 0:
            raise ValueError("Denominator cannot be zero.")
        return num, denom
    except ValueError as e:
        raise ValueError(f"Invalid ratio format or value: {e}")

def simplify_ratio(num, denom):
    common_divisor = gcd(num, denom)
    return num // common_divisor, denom // common_divisor

def simplify_ratios(ratio_dict):
    simplified_dict = {}
    for name, ratio in ratio_dict.items():
        num, denom = parse_ratio(ratio)
        simplified_num, simplified_denom = simplify_ratio(num, denom)
        simplified_dict[name] = f"{simplified_num}:{simplified_denom}"
    return simplified_dict

if __name__ == '__main__':
    sample_ratios = {
        'ratio1': '4:8',
        'ratio2': '10:25',
        'ratio3': '7:21'
    }
    print(simplify_ratios(sample_ratios))