def convert_weight_ratios(ratios):
    converted = []
    for num, denom in ratios:
        gcd = compute_gcd(num, denom)
        converted.append((num // gcd, denom // gcd))
    return converted

def compute_gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a
if __name__ == '__main__':
    sample_ratios = [(1000000000, 500000000), (2000000000, 1000000000), (3000000000, 1500000000)]
    converted_ratios = convert_weight_ratios(sample_ratios)
    print(converted_ratios)