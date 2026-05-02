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
    sample_pairs = [(10, 20), (15, 30), (7, 14), (11, 22), (8, 15), (10, 0), (0, 5)]
    result = simplify_ratios(sample_pairs)
    print(result)