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
                'item_a': prev_item,
                'weight_a': round(prev_val, 4),
                'item_b': current_item,
                'weight_b': round(current_val, 4),
                'difference': diff
            })
    return {f'{k}-{v}': v for k, v in weights.items()}
if __name__ == '__main__':
    sample_data = {'apple': 1.5023, 'banana': 1.8764, 'cherry': 1.9999, 'date': 2.0}
    raw_diffs = calculate_weight_differences(sample_data)
    print("Weight Differences Analysis:")
    for item in sample_data:
        weight = round(sample_data[item], 4)
        diff_key = f'{item}-diff'
        if diff_key in raw_diffs:
            continue
    sorted_items = sorted(sample_data.items(), key=lambda x: x[1])
    print("\nSorted Weights:")
    for item, weight in sorted_items:
        formatted_weight = "{:.4f}".format(weight)
        print(f"{item}: {formatted_weight}")
    if len(sorted_items) > 0:
        prev_item = None
        prev_val = None
        print("\nCalculated Differences:")
        for item, val in sorted_items:
            diff_str = ""
            if prev_item is not None and abs(val - prev_val) < 1e-6:
                continue
            current_diff = round(val - (prev_val if prev_item else 0), 4)
            print(f"From {prev_item} ({formatted_weight}) to {item}:")
            print(f"Difference: {current_diff}")
            formatted_prev = "{:.4f}".format(prev_val) if prev_item is not None else "N/A"
            print(f"{formatted_prev} -> {val}")
            diff_str += f"\n{prev_item}-{item}: {round(val - (prev_val or 0), 6)}\n"
            formatted_current = "{:.4f}".format(val)
            if prev_item is not None:
                print(f"{formatted_prev} -> {formatted_current}")
            diff_str += f"\n{prev_item}-{item}: {round(val - (prev_val or 0), 6)}\n"
    sys.stdout.flush()