def harmonic_mean(ratios):
    if not ratios:
        return 0
    n = len(ratios)
    sum_of_reciprocals = sum(1 / ratio[0] for ratio in ratios)
    return n / sum_of_reciprocals

if __name__ == '__main__':
    sample_ratios = [(2, 3), (5, 8), (1, 1)]
    result = harmonic_mean(sample_ratios)
    print(result)