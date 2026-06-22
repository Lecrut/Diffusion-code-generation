from math import gcd

def simplify_ratios(pairs):
    simplified_pairs = []
    for a, b in pairs:
        common_divisor = gcd(a, b)
        simplified_pair = (a // common_divisor, b // common_divisor)
        simplified_pairs.append(simplified_pair)
    return simplified_pairs

if __name__ == '__main__':
    sample_pairs = [(4, 8), (10, 15), (21, 6), (7, 3)]
    simplified_ratios_result = simplify_ratios(sample_pairs)
    print(simplified_ratios_result)