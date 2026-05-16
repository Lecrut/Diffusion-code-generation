import math
def convert_ratios_to_weights(ratios, total_weight):
    if not ratios:
        return []
    sum_ratios = sum(ratios)
    if sum_ratios == 0:
        return [0.0] * len(ratios)
    weights = []
    for ratio in ratios:
        weight = (ratio / sum_ratios) * total_weight
        weights.append(weight)
    return weights
if __name__ == '__main__':
    sample_ratios = {
        "A": 1.0,
        "B": 2.0,
        "C": 3.0
    }
    total_weight_value = 150.0
    ratio_list = [sample_ratios[key] for key in sorted(sample_ratios.keys())]
    absolute_weights = convert_ratios_to_weights(ratio_list, total_weight_value)
    print(f"Ratios: {ratio_list}")
    print(f"Total Weight: {total_weight_value}")
    print(f"Absolute Weights: {absolute_weights}")