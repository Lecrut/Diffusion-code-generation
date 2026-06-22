def extract_ids(dicts):
    return list(map(lambda d: d['id'], dicts))

if __name__ == '__main__':
    sample_dicts = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    print(extract_ids(sample_dicts))