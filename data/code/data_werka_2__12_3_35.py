from fractions import Fraction

def simplify_ratios(weight_ratios):
    simplified_ratios = []
    for ratio in weight_ratios:
        try:
            simplified_ratio = str(Fraction(ratio).limit_denominator())
            simplified_ratios.append(simplified_ratio)
        except ValueError as e:
            raise ValueError(f'Invalid ratio: {ratio}') from e
    return simplified_ratios
if __name__ == '__main__':
    sample_ratios = [0.5, 1.25, 0.75, 2.5, 3.75]
    print(simplify_ratios(sample_ratios))