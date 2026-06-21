def sort_dicts_by_key(dicts, key):
    if not all(isinstance(d, dict) for d in dicts):
        raise ValueError("All elements must be dictionaries")
    if key not in dicts[0]:
        raise KeyError(f"Key '{key}' not found in dictionary keys")
    return sorted(dicts, key=lambda x: x[key])

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_data = sort_dicts_by_key(sample_data, 'age')
    print(sorted_data)