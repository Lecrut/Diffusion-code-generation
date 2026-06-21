def convert_ratios_to_weights(ratios, total_weight):
    if not ratios:
        raise ValueError("Ratios list cannot be empty")
    
    ratio_sum = sum(ratios)
    if ratio_sum == 0:
        raise ValueError("Sum of ratios must not be zero")
    
    weights = [ratio / ratio_sum * total_weight for ratio in ratios]
    return weights

if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    sample_total_weight = 60
    absolute_weights = convert_ratios_to_weights(sample_ratios, sample_total_weight)
    print(absolute_weights)