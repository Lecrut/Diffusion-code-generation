import numpy as np

def calculate_ratio_conversion(base_weight, weight_ratios):
    base_weight_array = np.full_like(weight_ratios, base_weight, dtype=float)
    converted_weights = base_weight_array * weight_ratios
    return converted_weights
if __name__ == '__main__':
    base_weight = 100.0
    weight_ratios = [0.25, 0.5, 0.75, 1.0]
    result = calculate_ratio_conversion(base_weight, weight_ratios)
    print(result)