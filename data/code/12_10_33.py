def calculate_weight_distribution(weight_ratios, total_weight):
    if not weight_ratios:
        raise ValueError("Weight ratios dictionary cannot be empty")
    
    total_ratio = sum(weight_ratios.values())
    if total_ratio == 0:
        raise ValueError("Total ratio cannot be zero")
    
    distribution = {}
    for item, ratio in weight_ratios.items():
        try:
            distribution[item] = (ratio / total_ratio) * total_weight
        except ZeroDivisionError:
            distribution[item] = 0
    
    return distribution

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    sample_total_weight = 100
    result = calculate_weight_distribution(sample_ratios, sample_total_weight)
    print(result)