def convert_weight_ratios(ratios):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify_ratio(numerator, denominator):
        common_divisor = gcd(numerator, denominator)
        return numerator // common_divisor, denominator // common_divisor

    simplified_ratios = []
    for ratio in ratios:
        num, denom = map(int, ratio.split(':'))
        simplified_num, simplified_denom = simplify_ratio(num, denom)
        simplified_ratios.append(f"{simplified_num}:{simplified_denom}")
    
    return simplified_ratios

if __name__ == '__main__':
    sample_ratios = ["100:25", "450:300", "8000:6000"]
    result = convert_weight_ratios(sample_ratios)
    print(result)