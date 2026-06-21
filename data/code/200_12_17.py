def extract_keys(data, keys):
    return list(map(lambda x: {k: x.get(k) for k in keys if k in x}, data))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'id': 2, 'name': 'Bob', 'age': 30, 'city': 'Los Angeles'},
        {'id': 3, 'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
    ]
    keys_to_extract = ['id', 'name']
    result = extract_keys(sample_data, keys_to_extract)
    print(result)