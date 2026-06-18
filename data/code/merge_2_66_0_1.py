import sys
def calculate_weight_differences(weights):
    if not weights:
        return {}
    sorted_weights = sorted(weights.items(), key=lambda x: abs(x[1]))
    differences = []
    for i in range(1, len(sorted_weights)):
        current_item, current_val = sorted_weights[i]
        prev_item, prev_val = sorted_weights[i-1]
        diff = round(current_val - prev_val, 6)
        if abs(diff) > 0.0:
            differences.append({
                'item_1': prev_item,
                'weight_1': float(prev_val),
                'item_2': current_item,
                'weight_2': float(current_val),
                'difference': diff
            })
    return {f'pair_{i+1}': d for i, d in enumerate(differences)}
if __name__ == '__main__':
    sample_data = {'apple': 0.54321, 'banana': 0.67890, 'cherry': 0.54322, 'date': 0.67891}
    result = calculate_weight_differences(sample_data)
    print("Weight Differences Calculation Result:")
    for key in sorted(result.keys()):
        item_1 = result[key]['item_1']
        weight_1 = result[key]['weight_1']
        item_2 = result[key]['item_2']
        weight_2 = result[key]['weight_2']
        diff = result[key]['difference']
        print(f"Pair {key}:")
        print(f"  Item: {item_1} (Weight: {weight_1}) vs {item_2} (Weight: {weight_2})")
        print(f"  Difference: {diff}")