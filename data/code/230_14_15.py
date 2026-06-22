def extract_ids(dict_list):
    return list(map(lambda x: x['id'], dict_list))

if __name__ == '__main__':
    sample_dicts = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    print(extract_ids(sample_dicts))