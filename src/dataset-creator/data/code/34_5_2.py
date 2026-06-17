def merge_unique_dicts(list_of_dicts):
    merged = {}
    for item in list_of_dicts:
        if isinstance(item, dict) and not any(merged.get(k) is None for k in item.keys()):
            new_entry = True
            for key, value in item.items():
                if merged.get(key):
                    new_entry = False
                    break
            if new_entry:
                merged.update(item)
    return merged
if __name__ == '__main__':
    sample_data = [
        {'id': 101, 'name': 'Alice', 'age': 30},
        {'id': 102, 'name': 'Bob'},
        {'id': 103, 'email': 'charlie@example.com'},
        {'id': 104, 'name': 'David'}
    ]
    result = merge_unique_dicts(sample_data)
    print(result)