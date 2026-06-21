def extract_keys(data, keys):
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All items in the data list must be dictionaries.")
    if not isinstance(keys, list) or not all(isinstance(key, str) for key in keys):
        raise ValueError("The keys parameter must be a list of strings.")

    return list(map(lambda x: {k: x.get(k) for k in keys if k in x}, data))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    keys_to_extract = ['id', 'name']
    
    try:
        result = extract_keys(sample_data, keys_to_extract)
        print(result)
    except ValueError as e:
        print(e)