def convert_ratios_to_weights(ratios, total_weight):
    ratios_sum = sum(ratios)
    weights = [ratio / ratios_sum * total_weight for ratio in ratios]
    return weights

if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    specified_total_weight = 60
    absolute_weights = convert_ratios_to_weights(sample_ratios, specified_total_weight)
    print(absolute_weights)