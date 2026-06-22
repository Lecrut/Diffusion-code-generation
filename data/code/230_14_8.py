def extract_ids(dict_list):
    return list(map(lambda d: d['id'], dict_list))

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'}
    ]
    print(extract_ids(sample_data))