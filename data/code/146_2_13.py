def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda d: d[key])

if __name__ == '__main__':
    sample_dicts = [
        {'id': 3, 'value': 'apple'},
        {'id': 1, 'value': 'banana'},
        {'id': 2, 'value': 'cherry'}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'id')
    print(sorted_dicts)