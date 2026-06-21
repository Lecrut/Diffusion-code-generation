def validate_dicts(dicts):
    if not all(isinstance(d, dict) for d in dicts):
        raise ValueError("All items in the list must be dictionaries.")

def validate_key(key):
    if not isinstance(key, str):
        raise ValueError("Key must be a string.")

def sort_dicts_by_key(dicts, key):
    validate_dicts(dicts)
    validate_key(key)
    return sorted(dicts, key=lambda d: d.get(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts_age = sort_dicts_by_key(sample_dicts, 'age')
    print(sorted_dicts_age)