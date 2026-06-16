def apply_multiplier(ratios, multiplier):
    new_ratios = []
    for ratio in ratios:
        new_ratios.append((ratio[0] * multiplier, ratio[1]))
    return new_ratios
if __name__ == '__main__':
    sample_ratios = [(1, 2), (3, 4), (5, 6)]
    sample_multiplier = 1.5
    result = apply_multiplier(sample_ratios, sample_multiplier)
    print(result)