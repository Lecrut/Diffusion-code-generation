def convert_weight_ratios(ratios):
    from math import gcd
    simplified_ratios = []
    for num, denom in ratios:
        common_divisor = gcd(num, denom)
        simplified_num = num // common_divisor
        simplified_denom = denom // common_divisor
        simplified_ratios.append((simplified_num, simplified_denom))
    return simplified_ratios
if __name__ == '__main__':
    sample_ratios = [(100, 25), (81, 27), (45, 10), (60, 90)]
    print(convert_weight_ratios(sample_ratios))