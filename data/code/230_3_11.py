def flatten_dicts(dicts, keys):
    return [d[key] for d in dicts for key in keys if key in d]

if __name__ == '__main__':
    sample_dicts = [
        {'a': 1, 'b': 2},
        {'a': 3, 'c': 4},
        {'b': 5}
    ]
    keys_to_extract = ['a', 'b']
    result = flatten_dicts(sample_dicts, keys_to_extract)
    print(result)