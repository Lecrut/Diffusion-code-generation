def extract_ids(data):
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All items in the list must be dictionaries.")
    return list(map(lambda d: d['id'], data))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'}
    ]
    ids = extract_ids(sample_data)
    print(ids)