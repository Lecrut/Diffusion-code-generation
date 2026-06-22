def harmonic_mean(ratios):
    if not all(len(ratio) == 2 and isinstance(ratio[0], (int, float)) and isinstance(ratio[1], (int, float)) for ratio in ratios):
        raise ValueError("Ratios must be tuples of two numbers.")
    
    total = sum(1 / ratio[0] * ratio[1] for ratio in ratios)
    if total == 0:
        raise ValueError("Total cannot be zero.")
    
    return len(ratios) / total

if __name__ == '__main__':
    sample_ratios = [(2, 3), (5, 8), (1, 1)]
    result = harmonic_mean(sample_ratios)
    print(result)