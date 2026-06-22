def calculate_ratio_conversion(base_weight, weight_ratios):
    return [base_weight * ratio for ratio in weight_ratios]

if __name__ == '__main__':
    base_weight = 100.0
    weight_ratios = [0.5, 1.0, 1.5, 2.0]
    converted_weights = calculate_ratio_conversion(base_weight, weight_ratios)
    print(converted_weights)