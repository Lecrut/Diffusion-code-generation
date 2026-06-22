def validate_ratios(ratios):
    if not all(isinstance(ratio, tuple) and len(ratio) == 2 for ratio in ratios):
        raise ValueError("All elements must be tuples of two numbers")

def harmonic_mean_of_ratios(ratios):
    validate_ratios(ratios)
    n = len(ratios)
    sum_reciprocals = sum(1 / (ratio[0] / ratio[1]) for ratio in ratios)
    return n / sum_reciprocals

if __name__ == '__main__':
    sample_ratios = [(2, 3), (5, 8), (1, 1)]
    result = harmonic_mean_of_ratios(sample_ratios)
    print(result)