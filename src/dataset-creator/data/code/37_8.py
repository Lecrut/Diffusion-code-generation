import json
def merge_and_update_counts(data_list):
    counts = {}
    for item in data_list:
        if isinstance(item, dict) and 'item' in item:
            current_item = item['item']
            count = counts.get(current_item, 0) + 1
            counts[current_item] = count
    return counts
def process_large_dataset(input_data):
    processed_items = [d for d in input_data if isinstance(d, dict)]
    final_counts = merge_and_update_counts(processed_items)
    result_list = [{'item': k, 'count': v} for k, v in sorted(final_counts.items())]
    return json.dumps(result_list)
if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'item': 'apple', 'qty': 5},
        {'id': 102, 'item': 'banana', 'qty': 3},
        {'id': 103, 'item': 'apple', 'qty': 2},
        {'id': 104, 'item': 'cherry', 'qty': 8},
        {'id': 105, 'item': 'banana', 'qty': 7}
    ]
    output = process_large_dataset(sample_data)
    print(output)