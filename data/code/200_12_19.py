def validate_data(data):
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All elements in the list must be dictionaries")
    return data

def extract_keys(data, keys):
    return list(map(lambda x: {k: x.get(k) for k in keys if k in x}, validate_data(data)))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    keys_to_extract = ['id', 'name']
    result = extract_keys(sample_data, keys_to_extract)
    print(result)