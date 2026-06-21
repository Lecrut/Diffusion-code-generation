def validate_input(base_weight, weight_ratios):
    if not isinstance(base_weight, (int, float)):
        raise ValueError("Base weight must be an integer or float.")
    if not isinstance(weight_ratios, list):
        raise ValueError("Weight ratios must be a list.")
    if not all(isinstance(ratio, (int, float)) for ratio in weight_ratios):
        raise ValueError("All weight ratios must be integers or floats.")

def calculate_ratio_conversion(base_weight, weight_ratios):
    validate_input(base_weight, weight_ratios)
    return [base_weight * ratio for ratio in weight_ratios]

if __name__ == '__main__':
    base_weight = 150.0
    weight_ratios = [0.33, 0.67, 1.0, 1.33]
    converted_weights = calculate_ratio_conversion(base_weight, weight_ratios)
    print(converted_weights)