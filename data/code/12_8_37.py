def calculate_ratio_conversion(base_weight, weight_ratios):
    if not isinstance(base_weight, (int, float)) or base_weight <= 0:
        raise ValueError("Base weight must be a positive number.")
    
    if not all(isinstance(ratio, (int, float)) and ratio > 0 for ratio in weight_ratios):
        raise ValueError("All weight ratios must be positive numbers.")
    
    converted_weights = [base_weight * ratio for ratio in weight_ratios]
    return converted_weights

if __name__ == '__main__':
    base_weight = 100
    weight_ratios = [0.5, 1.2, 1.5, 2.0]
    result = calculate_ratio_conversion(base_weight, weight_ratios)
    print(result)