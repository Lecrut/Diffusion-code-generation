def simplify_ratios(pairs):
    simplified = []
    for a, b in pairs:
        import math
        if b == 0:
            simplified.append((float('inf'), 0.0))
        else:
            common = math.gcd(a, b)
            simplified.append((a // common, b // common))
    return simplified
if __name__ == '__main__':
    sample_pairs = [(6, 9), (10, 25), (12, 18), (7, 14), (15, 0)]
    result = simplify_ratios(sample_pairs)
    print(result)