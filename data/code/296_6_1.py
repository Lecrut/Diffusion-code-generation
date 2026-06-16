def apply_multiplier(ratios, multiplier):
    new_ratios = []
    for ratio in ratios:
        new_ratios.append((ratio[0] * multiplier, ratio[1]))
    return new_ratios
if __name__ == '__main__':
    sample_ratios = [(2, 3), (5, 8), (1, 1)]
    multiplier_value = 1.5
    result = apply_multiplier(sample_ratios, multiplier_value)
    print(result)