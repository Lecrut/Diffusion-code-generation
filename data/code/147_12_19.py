def validate_key_and_data(data, key):
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All elements must be dictionaries")
    if not any(key in item for item in data):
        raise KeyError(f"Key '{key}' not found in any dictionary")

def sort_dicts_by_key(data, key):
    validate_key_and_data(data, key)
    return sorted(data, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    key_to_sort_by = 'age'
    
    sorted_data = sort_dicts_by_key(sample_data, key_to_sort_by)
    print(sorted_data)