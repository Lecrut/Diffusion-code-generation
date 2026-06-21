def validate_dicts(dicts):
    if not all(isinstance(d, dict) for d in dicts):
        raise ValueError("All elements must be dictionaries")
    return dicts

def sort_dicts_by_key(dicts, key):
    validated_dicts = validate_dicts(dicts)
    if key not in validated_dicts[0]:
        raise KeyError(f"Key '{key}' not found in dictionary keys")
    return sorted(validated_dicts, key=lambda x: x[key])

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'age')
    print(sorted_dicts)