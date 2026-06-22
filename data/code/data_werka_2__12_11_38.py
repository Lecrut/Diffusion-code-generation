def convert_ratios_to_weights(ratios, total_weight):
    if not ratios or total_weight <= 0:
        raise ValueError("Invalid input: ratios must be non-empty and total weight must be positive.")
    
    ratio_sum = sum(ratios)
    if ratio_sum == 0:
        raise ValueError("Invalid input: sum of ratios must be greater than zero.")
    
    weights = [ratio * total_weight / ratio_sum for ratio in ratios]
    return weights

if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    sample_total_weight = 60
    try:
        absolute_weights = convert_ratios_to_weights(sample_ratios, sample_total_weight)
        print(absolute_weights)
    except ValueError as e:
        print(e)