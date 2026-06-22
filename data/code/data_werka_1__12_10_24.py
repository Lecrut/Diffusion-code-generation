def calculate_weight_distribution(weight_ratios, total_weight):
    if total_weight == 0:
        return {item: 0 for item in weight_ratios}
    
    total_ratio = sum(weight_ratios.values())
    if total_ratio == 0:
        return {item: 0 for item in weight_ratios}
    
    distribution = {}
    for item, ratio in weight_ratios.items():
        distribution[item] = (ratio / total_ratio) * total_weight
    
    return distribution

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    sample_total_weight = 100
    result = calculate_weight_distribution(sample_ratios, sample_total_weight)
    print(result)