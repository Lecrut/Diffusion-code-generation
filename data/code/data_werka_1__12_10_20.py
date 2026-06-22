def calculate_weight_distribution(weight_ratios, total_weight):
    if not weight_ratios:
        return {}
    
    total_ratio = sum(weight_ratios.values())
    if total_ratio == 0:
        return {key: 0 for key in weight_ratios}
    
    distribution = {key: (value / total_ratio) * total_weight for key, value in weight_ratios.items()}
    return distribution

if __name__ == '__main__':
    sample_ratios = {'A': 2, 'B': 3}
    sample_total_weight = 100
    result = calculate_weight_distribution(sample_ratios, sample_total_weight)
    print(result)