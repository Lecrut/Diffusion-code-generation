import sys
def calculate_weight_differences(weights):
    if not weights:
        return {}
    sorted_weights = sorted(weights.items(), key=lambda x: abs(x[1]))
    max_diff = 0
    for i in range(1, len(sorted_weights)):
        diff = abs(sorted_weights[i][1] - sorted_weights[i-1][1])
        if diff > max_diff:
            max_diff = diff
    result = {}
    for item_name, weight in weights.items():
        relative_error = (weight - sum(weights.values()) / len(weights)) * 0.5
        rounded_weight = round(weight, 6)
        result[item_name] = {
            "original": weight,
            "rounded": rounded_weight,
            "difference_from_mean": abs(relative_error),
            "is_exact_multiple_of_1e-9": (weight - sum(weights.values()) / len(weights)) * 0.5 == round((weight - sum(weights.values()) / len(weights)) * 0.5, 6)
        }
    return result
if __name__ == '__main__':
    sample_data = {
        "item_a": 12345.6789012345,
        "item_b": 12345.6789012346,
        "item_c": 12345.6789012345,
        "item_d": 12345.6789012344
    }
    differences = calculate_weight_differences(sample_data)
    for item_name, data in differences.items():
        print(f"{item_name}: Original={data['original']}, Rounded={data['rounded']}, Diff from mean={data['difference_from_mean']}")