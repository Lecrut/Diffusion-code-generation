def extract_keys(data, keys):
    return list(map(lambda x: {k: x.get(k) for k in keys if k in x}, data))

if __name__ == '__main__':
    sample_data = [
        {'id': 4, 'name': 'David', 'age': 28},
        {'id': 5, 'name': 'Eve', 'age': 22},
        {'id': 6, 'name': 'Frank', 'age': 31}
    ]
    keys_to_extract = ['id', 'name']
    extracted_data = extract_keys(sample_data, keys_to_extract)
    print(extracted_data)