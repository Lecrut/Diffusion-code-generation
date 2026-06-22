from math import gcd

def validate_pair(pair):
    if not isinstance(pair, tuple) or len(pair) != 2:
        raise ValueError("Each pair must be a tuple of two elements.")
    if not all(isinstance(x, int) and x > 0 for x in pair):
        raise ValueError("Both elements of the pair must be positive integers.")

def simplify_ratios(pairs):
    simplified_pairs = []
    for pair in pairs:
        validate_pair(pair)
        a, b = pair
        common_divisor = gcd(a, b)
        simplified_a = a // common_divisor
        simplified_b = b // common_divisor
        simplified_pairs.append((simplified_a, simplified_b))
    return simplified_pairs

if __name__ == '__main__':
    sample_pairs = [(12, 18), (20, 35), (9, 27), (8, 16)]
    print(simplify_ratios(sample_pairs))