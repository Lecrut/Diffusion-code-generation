def convert_ratios_to_weights(ratios, total_weight):
    ratios_sum = sum(ratios)
    return [ratio / ratios_sum * total_weight for ratio in ratios]

if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    total_weight = 60
    absolute_weights = convert_ratios_to_weights(sample_ratios, total_weight)
    print(absolute_weights)