def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x[key])

if __name__ == '__main__':
    sample_data = [
        {'id': 3, 'value': 'banana'},
        {'id': 1, 'value': 'apple'},
        {'id': 2, 'value': 'cherry'}
    ]
    sorted_data = sort_dicts_by_key(sample_data, 'id')
    print(sorted_data)