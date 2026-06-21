def calculate_ratio_conversion(base_weight, weight_ratios):
    if not isinstance(base_weight, (int, float)):
        raise ValueError("Base weight must be an integer or float.")
    if not all(isinstance(ratio, (int, float)) for ratio in weight_ratios):
        raise ValueError("All weight ratios must be integers or floats.")
    
    converted_weights = [base_weight * ratio for ratio in weight_ratios]
    return converted_weights

if __name__ == '__main__':
    base_weight = 100.0
    weight_ratios = [0.5, 1.2, 1.5, 2.0]
    result = calculate_ratio_conversion(base_weight, weight_ratios)
    print(result)