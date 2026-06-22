def harmonic_mean_of_ratios(ratios):
    if not all(isinstance(ratio, tuple) and len(ratio) == 2 for ratio in ratios):
        raise ValueError("Input must be a list of tuples, each with two elements.")
    
    try:
        sum_reciprocals = sum(1 / (ratio[0] / ratio[1]) for ratio in ratios)
        return len(ratios) / sum_reciprocals
    except ZeroDivisionError:
        raise ValueError("Ratios must not be zero.")

if __name__ == '__main__':
    sample_ratios = [(2, 3), (4, 5), (6, 7)]
    result = harmonic_mean_of_ratios(sample_ratios)
    print(result)