def calculate_ratio_conversion(base_weight, weight_ratios):
    converted_weights = []
    for ratio in weight_ratios:
        converted_weight = base_weight * ratio
        converted_weights.append(converted_weight)
    return converted_weights

if __name__ == '__main__':
    BASE_WEIGHT = 200.0
    WEIGHT_RATIOS = [0.1, 0.3, 0.6, 0.9]
    result = calculate_ratio_conversion(BASE_WEIGHT, WEIGHT_RATIOS)
    print(result)