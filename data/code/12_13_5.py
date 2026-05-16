def calculate_weight_distribution(ratios, total_weight):
    distribution = {}
    if total_weight == 0:
        for item in ratios:
            distribution[item] = 0.0
        return distribution
    for item, ratio in ratios.items():
        if ratio == 0:
            distribution[item] = 0.0
        else:
            actual_weight = (ratio / sum(ratios.values())) * total_weight
            distribution[item] = actual_weight
    return distribution
if __name__ == '__main__':
    weight_ratios = {'A': 2, 'B': 3, 'C': 1}
    total_weight = 100
    result = calculate_weight_distribution(weight_ratios, total_weight)
    print(result)