def convert_weight_ratios(ratios):
    from fractions import Fraction
    return [Fraction(ratio).limit_denominator() for ratio in ratios]
if __name__ == '__main__':
    sample_ratios = [1000000000, 2500000000, 7500000000, 15000000000]
    converted_ratios = convert_weight_ratios(sample_ratios)
    print(converted_ratios)