from math import gcd

def simplify_ratios(pairs):
    simplified_pairs = []
    for a, b in pairs:
        common_divisor = gcd(a, b)
        simplified_pairs.append((a // common_divisor, b // common_divisor))
    return simplified_pairs

if __name__ == '__main__':
    sample_pairs = [(100, 25), (81, 27), (48, 64)]
    print(simplify_ratios(sample_pairs))