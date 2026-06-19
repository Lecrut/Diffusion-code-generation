def convert_ratios_to_weights(ratios, total_weight):
    ratio_sum = sum(ratios)
    weights = [ratio / ratio_sum * total_weight for ratio in ratios]
    return weights
if __name__ == '__main__':
    ratios = [1, 2, 3]
    total_weight = 60
    weights = convert_ratios_to_weights(ratios, total_weight)
    print(weights)