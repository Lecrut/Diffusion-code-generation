def calculate_ratio_conversion(base_weight, weight_ratios):
    converted_weights = [base_weight * ratio for ratio in weight_ratios]
    return converted_weights

if __name__ == '__main__':
    base_weight = 100.0
    weight_ratios = [0.5, 1.2, 1.5, 2.0]
    result = calculate_ratio_conversion(base_weight, weight_ratios)
    print(result)