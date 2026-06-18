import sys
def calculate_weight_differences(weights_dict):
    if not weights_dict:
        return {}
    diffs = []
    items = list(weights_dict.items())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            item_a_name, weight_a = items[i]
            item_b_name, weight_b = items[j]
            diff = abs(weight_a - weight_b)
            diffs.append({
                'item_1': item_a_name,
                'weight_1': round(float(weight_a), 6),
                'item_2': item_b_name,
                'weight_2': round(float(weight_b), 6),
                'difference': diff
            })
    return diffs
def main():
    sample_data = {
        "apple": 1.50349876,
        "banana": 0.78912345,
        "cherry": 2.12345678,
        "date": 0.98765432
    }
    results = calculate_weight_differences(sample_data)
    print("Weight Differences Report:")
    for result in results:
        print(f"Item {result['item_1']} ({result['weight_1']}) vs Item {result['item_2']} ({result['weight_2']})")
        print(f"Difference: {result['difference']}")
if __name__ == '__main__':
    main()