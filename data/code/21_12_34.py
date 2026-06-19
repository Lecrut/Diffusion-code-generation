def validate_key_in_dicts(dicts, key):
    for d in dicts:
        if key not in d:
            raise ValueError(f"Key '{key}' not found in one of the dictionaries.")

def sort_dicts_by_key(dicts, key):
    validate_key_in_dicts(dicts, key)
    return sorted(dicts, key=lambda x: x[key], reverse=True)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_data = sort_dicts_by_key(sample_data, 'age')
    print(sorted_data)