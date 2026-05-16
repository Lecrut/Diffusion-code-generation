import math
def calculate_ratio_conversion(base_weight, ratios):
    converted_weights = {}
    for ratio in ratios:
        converted_weights[ratio] = base_weight * ratio
    return converted_weights
if __name__ == '__main__':
    base = 100.0
    ratios_list = [1.5, 0.8, 2.0, 3.14159]
    results = calculate_ratio_conversion(base, ratios_list)
    print(results)