def filter_dicts(dicts, keys):
    return [{key: d[key] for key in keys if key in d} for d in dicts]

if __name__ == '__main__':
    sample_dicts = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 4, 'd': 5, 'e': 6}
    ]
    keys_to_extract = ['a', 'c']
    filtered_dicts = filter_dicts(sample_dicts, keys_to_extract)
    print(filtered_dicts)