def validate_ratios(ratios):
    if not all(isinstance(ratio, tuple) and len(ratio) == 2 for ratio in ratios):
        raise ValueError("All elements must be tuples of two numbers.")
    if any(not (isinstance(num, (int, float)) and num > 0) for ratio in ratios for num in ratio):
        raise ValueError("Both elements of each tuple must be positive numbers.")

def calculate_harmonic_mean(ratios):
    validate_ratios(ratios)
    denominators = [1 / ratio[0] * ratio[1] for ratio in ratios]
    harmonic_sum = sum(denominators)
    if harmonic_sum == 0:
        raise ValueError("Harmonic mean is undefined when the sum of denominators is zero.")
    return len(ratios) / harmonic_sum

if __name__ == '__main__':
    sample_ratios = [(1, 2), (3, 4), (5, 6)]
    result = calculate_harmonic_mean(sample_ratios)
    print(result)