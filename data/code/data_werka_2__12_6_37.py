def convert_weight_ratios(ratios):
    gcd = lambda x, y: gcd(y, x % y) if y else x
    lcm = lambda x, y: x * y // gcd(x, y)
    total_lcm = 1
    for ratio in ratios:
        total_lcm = lcm(total_lcm, ratio)
    normalized_ratios = [total_lcm // ratio for ratio in ratios]
    return normalized_ratios
if __name__ == '__main__':
    sample_ratios = [123456789012345, 987654321098765, 111111111111111]
    normalized = convert_weight_ratios(sample_ratios)
    print(normalized)