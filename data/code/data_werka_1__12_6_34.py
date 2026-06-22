def convert_weight_ratios(ratios):
    result = []
    for ratio in ratios:
        numerator, denominator = map(int, ratio.split(':'))
        gcd = compute_gcd(numerator, denominator)
        optimized_ratio = (numerator // gcd, denominator // gcd)
        result.append(optimized_ratio)
    return result

def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    sample_ratios = ['100:25', '81:27', '48:16']
    optimized_ratios = convert_weight_ratios(sample_ratios)
    print(optimized_ratios)