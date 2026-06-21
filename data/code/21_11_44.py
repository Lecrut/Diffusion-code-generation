SORT_KEY = 'age'

def sort_dicts_by_key(dicts, key=SORT_KEY):
    if not isinstance(dicts, list) or not all(isinstance(d, dict) for d in dicts):
        raise ValueError("Input must be a list of dictionaries.")
    if not isinstance(key, str):
        raise ValueError("Key must be a string.")
    return sorted(dicts, key=lambda x: x.get(key), reverse=True)

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', SORT_KEY: 30},
        {'name': 'Bob', SORT_KEY: 25},
        {'name': 'Charlie', SORT_KEY: 35}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts)
    print(sorted_dicts)