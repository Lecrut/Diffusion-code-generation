def convert_weight_ratios(ratios):
    from fractions import Fraction
    return [Fraction(r).limit_denominator() for r in ratios]

if __name__ == '__main__':
    sample_ratios = [12345678901234567890, 98765432109876543210, 11111111111111111111]
    converted_ratios = convert_weight_ratios(sample_ratios)
    print(converted_ratios)