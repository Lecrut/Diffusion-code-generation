import json
def merge_and_update_counts(data_list):
    counts = {}
    for item in data_list:
        if isinstance(item, dict) and 'item_id' in item:
            current_count = counts.get(item['item_id'], 0) + 1
            counts[item['item_id']] = current_count
        elif isinstance(item, str):
            word_counts = {}
            for char in item.lower():
                if not char.isalnum():
                    continue
                count = word_counts.get(char, 0) + 1
                word_counts[char] = count
    return counts
def process_large_dataset(file_path=None, sample_data=None):
    if file_path:
        with open(file_path, 'r') as f:
            data_list = json.load(f)
    elif isinstance(sample_data, list):
        data_list = sample_data
    else:
        raise ValueError("No input provided")
    counts_dict = {}
    for item in data_list:
        if isinstance(item, dict):
            item_id = item.get('item_id', 'unknown')
            current_count = counts_dict.get(item_id, 0) + 1
            counts_dict[item_id] = current_count
    return counts_dict
if __name__ == '__main__':
    sample_data = [
        {'item_id': 'A'},
        {'item_id': 'B'},
        {'item_id': 'C'},
        {'item_id': 'D'},
        {'item_id': 'E'}
    ] * 10
    result_counts = process_large_dataset(sample_data=sample_data)
    print(json.dumps(result_counts, indent=2))