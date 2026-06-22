def convert_ratios_to_weights(ratios, total_weight):
    total_ratio = sum(ratios)
    return [ratio / total_ratio * total_weight for ratio in ratios]

if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    specified_total_weight = 60
    absolute_weights = convert_ratios_to_weights(sample_ratios, specified_total_weight)
    print(absolute_weights)