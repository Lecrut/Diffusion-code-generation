def convert_weight_ratios(ratios):
    import math
    gcd_values = [math.gcd(a, b) for a, b in ratios]
    normalized_ratios = [(a // gcd, b // gcd) for (a, b), gcd in zip(ratios, gcd_values)]
    return normalized_ratios

if __name__ == '__main__':
    sample_ratios = [(1024000000, 768000000), (123456789, 987654321), (100000000, 25000000)]
    print(convert_weight_ratios(sample_ratios))