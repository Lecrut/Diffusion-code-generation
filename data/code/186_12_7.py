def validate_dicts(dicts):
    if not all(isinstance(d, dict) for d in dicts):
        raise ValueError("All elements must be dictionaries")

def sort_dicts_by_key(dicts, key):
    validate_dicts(dicts)
    return sorted(dicts, key=lambda x: x[key])

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'age')
    print(sorted_dicts)