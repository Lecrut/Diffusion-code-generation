def dict_equal(d1, d2):
    if d1 is d2:
        return True
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        return False
    if len(d1) != len(d2):
        return False
    for k in d1:
        if k not in d2 or not dict_equal(d1[k], d2[k]):
            return False
    return True

if __name__ == '__main__':
    sample_a = {'key1': {'subkey1': 42, 'subkey2': [1, 2, 3]}, 'key2': 'value2'}
    sample_b = {'key1': {'subkey1': 42, 'subkey2': [1, 2, 3]}, 'key2': 'value2'}
    print(dict_equal(sample_a, sample_b))