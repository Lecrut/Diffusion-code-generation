def filter_dicts(dicts, keys):
    return [{k: d[k] for k in keys if k in d} for d in dicts]

if __name__ == '__main__':
    sample_dicts = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 4, 'b': 5, 'd': 6},
        {'b': 7, 'c': 8}
    ]
    keys_to_extract = ['a', 'b']
    filtered_dicts = filter_dicts(sample_dicts, keys_to_extract)
    print(filtered_dicts)