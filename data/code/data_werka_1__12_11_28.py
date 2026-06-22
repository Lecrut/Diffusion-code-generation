def convert_ratios_to_weights(ratios, total_weight):
    total_ratio = sum(ratios)
    weights = [ratio / total_ratio * total_weight for ratio in ratios]
    return weights

if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    sample_total_weight = 60
    absolute_weights = convert_ratios_to_weights(sample_ratios, sample_total_weight)
    print(absolute_weights)