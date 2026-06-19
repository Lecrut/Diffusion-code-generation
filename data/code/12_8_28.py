import numpy as np

def calculate_ratio_conversion(base_weight, weight_ratios):
    ratios_array = np.array(weight_ratios)
    converted_weights = base_weight * ratios_array
    return converted_weights.tolist()

if __name__ == '__main__':
    base_weight = 100.0
    weight_ratios = [0.25, 0.5, 0.75, 1.0]
    result = calculate_ratio_conversion(base_weight, weight_ratios)
    print(result)