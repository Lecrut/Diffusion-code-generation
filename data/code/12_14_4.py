def convert_ratios_to_weights(ratios, total_weight):
    weights = {}
    if not ratios:
        return weights
    ratio_sum = sum(ratios)
    if ratio_sum == 0:
        return {ratio: 0.0 for ratio in ratios}
    for ratio in ratios:
        weight = (ratio / ratio_sum) * total_weight
        weights[ratio] = weight
    return weights
if __name__ == '__main__':
    relative_ratios = [1, 2, 3]
    total_weight = 100.0
    absolute_weights = convert_ratios_to_weights(relative_ratios, total_weight)
    print(absolute_weights)