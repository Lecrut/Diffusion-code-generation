def harmonic_mean(ratios):
    sum_of_ratios = 0
    for ratio in ratios:
        sum_of_ratios += 1 / ratio[1]
    if sum_of_ratios == 0:
        return None
    return len(ratios) / sum_of_ratios

if __name__ == '__main__':
    sample_ratios = [(1, 2), (3, 4), (5, 6)]
    result = harmonic_mean(sample_ratios)
    print(result)