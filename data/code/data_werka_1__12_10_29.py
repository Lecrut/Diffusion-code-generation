def calculate_weight_distribution(weight_ratios, total_weight):
    if total_weight == 0:
        return {item: 0 for item in weight_ratios}
    
    sum_of_ratios = sum(weight_ratios.values())
    if sum_of_ratios == 0:
        return {item: 0 for item in weight_ratios}
    
    distribution = {}
    for item, ratio in weight_ratios.items():
        distribution[item] = (ratio / sum_of_ratios) * total_weight
    return distribution

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    total_weight = 100
    result = calculate_weight_distribution(sample_ratios, total_weight)
    print(result)