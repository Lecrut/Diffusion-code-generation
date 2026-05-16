import math
def calculate_ratio_conversion(base_weight, ratios):
    converted_weights = {}
    for ratio in ratios:
        if ratio == 0:
            converted_weights[ratio] = float('inf') if base_weight != 0 else float('nan')
        else:
            converted_weights[ratio] = base_weight * ratio
    return converted_weights
if __name__ == '__main__':
    base = 100.0
    ratios = [1.5, 0.5, 2.0, 0.0, -1.25]
    result = calculate_ratio_conversion(base, ratios)
    print(result)