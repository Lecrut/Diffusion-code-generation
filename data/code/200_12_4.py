def extract_keys(data, keys):
    return list(map(lambda x: {k: v for k, v in x.items() if k in keys}, data))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 25},
        {'id': 2, 'name': 'Bob', 'age': 30},
        {'id': 3, 'name': 'Charlie', 'age': 35}
    ]
    keys_to_extract = ['id', 'name']
    result = extract_keys(sample_data, keys_to_extract)
    print(result)