from math import gcd

def simplify_ratios(pairs):
    simplified_pairs = []
    for a, b in pairs:
        common_divisor = gcd(a, b)
        simplified_a = a // common_divisor
        simplified_b = b // common_divisor
        simplified_pairs.append((simplified_a, simplified_b))
    return simplified_pairs

if __name__ == '__main__':
    sample_values = [(4, 8), (10, 5), (7, 3), (20, 10)]
    print(simplify_ratios(sample_values))