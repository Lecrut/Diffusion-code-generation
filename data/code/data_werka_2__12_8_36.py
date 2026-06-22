def calculate_ratio_conversion(base_weight, weight_ratios):
    if not isinstance(base_weight, (int, float)):
        raise ValueError("Base weight must be an integer or float.")
    if not all(isinstance(ratio, (int, float)) for ratio in weight_ratios):
        raise ValueError("All weight ratios must be integers or floats.")
    
    return [base_weight * ratio for ratio in weight_ratios]

if __name__ == '__main__':
    base_weight = 50.0
    weight_ratios = [0.1, 0.2, 0.3, 0.4]
    converted_weights = calculate_ratio_conversion(base_weight, weight_ratios)
    print(converted_weights)