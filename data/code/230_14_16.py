def extract_ids(data):
    return list(map(lambda x: x['id'], data))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'}
    ]
    ids = extract_ids(sample_data)
    print(ids)