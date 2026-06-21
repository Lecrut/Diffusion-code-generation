def key_exists_in_dicts(key, list_of_dicts):
    return any((key in d for d in list_of_dicts))
if __name__ == '__main__':
    sample_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    print(key_exists_in_dicts('b', sample_dicts))
    print(key_exists_in_dicts('d', sample_dicts))