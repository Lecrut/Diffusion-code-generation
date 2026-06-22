from fractions import Fraction

def simplify_ratios(pairs):
    simplified_pairs = [(Fraction(a, b).numerator, Fraction(a, b).denominator) for a, b in pairs]
    return simplified_pairs

if __name__ == '__main__':
    sample_pairs = [(8, 12), (100, 25), (45, 10)]
    print(simplify_ratios(sample_pairs))