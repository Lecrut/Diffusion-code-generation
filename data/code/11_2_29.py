from math import gcd

def simplify_ratios(pairs):
    simplified_pairs = []
    for a, b in pairs:
        common_divisor = gcd(a, b)
        simplified_pairs.append((a // common_divisor, b // common_divisor))
    return simplified_pairs

if __name__ == '__main__':
    sample_values = [(4, 8), (10, 25), (7, 3), (60, 90)]
    print(simplify_ratios(sample_values))