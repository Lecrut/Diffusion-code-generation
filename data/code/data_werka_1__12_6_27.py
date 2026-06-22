def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def convert_weight_ratios(ratios):
    results = []
    for ratio in ratios:
        num, denom = map(int, ratio.split(':'))
        divisor = gcd(num, denom)
        simplified_ratio = (num // divisor, denom // divisor)
        results.append(simplified_ratio)
    return results

if __name__ == '__main__':
    sample_ratios = ["100000000:25000000", "8000000:4000000", "300000000:75000000"]
    converted_ratios = convert_weight_ratios(sample_ratios)
    print(converted_ratios)