def calculate_weight_distribution(weight_ratios, total_weight):
    if not weight_ratios:
        raise ValueError("Weight ratios dictionary cannot be empty")
    
    total_ratio = sum(weight_ratios.values())
    if total_ratio == 0:
        raise ValueError("Total ratio cannot be zero")
    
    distribution = {}
    for item, ratio in weight_ratios.items():
        distribution[item] = (ratio / total_ratio) * total_weight
    
    return distribution

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    total_weight = 100
    try:
        result = calculate_weight_distribution(sample_ratios, total_weight)
        print(result)
    except ValueError as e:
        print(e)