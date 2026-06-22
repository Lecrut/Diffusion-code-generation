def harmonic_mean(ratios):
    if not ratios:
        return 0
    sum_ratios = len(ratios)
    reciprocal_sum = sum(1 / ratio for ratio in ratios)
    return sum_ratios / reciprocal_sum

if __name__ == '__main__':
    sample_ratios = [2, 3, 4]
    result = harmonic_mean(sample_ratios)
    print(result)