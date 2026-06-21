def extract_keys(data, keys):
    return list(map(lambda x: {k: x.get(k) for k in keys if k in x}, data))

if __name__ == '__main__':
    sample_data = [
        {'id': 4, 'name': 'David', 'age': 40},
        {'id': 5, 'name': 'Eve', 'age': 45}
    ]
    keys_to_extract = ['id', 'name']
    result = extract_keys(sample_data, keys_to_extract)
    print(result)