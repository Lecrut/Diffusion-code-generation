def calculate_weight_distribution(ratios, total_weight):
    distribution = {}
    if total_weight == 0:
        for item in ratios:
            distribution[item] = 0
        return distribution
    total_ratio = sum(ratios.values())
    if total_ratio == 0:
        for item in ratios:
            distribution[item] = 0
        return distribution
    for item, ratio in ratios.items():
        if ratio != 0:
            actual_weight = (ratio / total_ratio) * total_weight
            distribution[item] = actual_weight
        else:
            distribution[item] = 0
    return distribution
if __name__ == '__main__':
    ratios_data = {'A': 2, 'B': 3, 'C': 1}
    total_w = 100
    result = calculate_weight_distribution(ratios_data, total_w)
    print(result)