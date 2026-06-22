def calculate_weight_distribution(weight_ratios, total_weight):
    if not weight_ratios:
        return {}
    
    total_ratio = sum(weight_ratios.values())
    if total_ratio == 0:
        return {item: 0 for item in weight_ratios}
    
    distribution = {item: (ratio / total_ratio) * total_weight for item, ratio in weight_ratios.items()}
    return distribution

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    total_weight = 100
    result = calculate_weight_distribution(sample_ratios, total_weight)
    print(result)