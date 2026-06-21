from math import gcd

def simplify_ratios(pairs):
    def simplify_pair(pair):
        a, b = pair
        common_divisor = gcd(a, b)
        return (a // common_divisor, b // common_divisor)

    simplified_pairs = [simplify_pair(pair) for pair in pairs]
    return simplified_pairs

if __name__ == '__main__':
    sample_pairs = [(12, 16), (15, 40), (8, 32), (9, 27)]
    simplified_ratios_result = simplify_ratios(sample_pairs)
    print(simplified_ratios_result)