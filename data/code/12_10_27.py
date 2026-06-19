def calculate_weight_distribution(weight_ratios, total_weight):
    if not weight_ratios or total_weight <= 0:
        return {}

    total_ratio = sum(weight_ratios.values())
    if total_ratio == 0:
        return {key: 0 for key in weight_ratios}

    distribution = {}
    for item, ratio in weight_ratios.items():
        distribution[item] = (ratio / total_ratio) * total_weight
    return distribution

if __name__ == '__main__':
    sample_weights = {'A': 2, 'B': 3}
    total_weight = 100
    result = calculate_weight_distribution(sample_weights, total_weight)
    print(result)