KEY_TO_CHECK = 'b'

def key_exists_in_dicts(key, dict_list):
    return any((key in d for d in dict_list))

if __name__ == '__main__':
    sample_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    print(key_exists_in_dicts(KEY_TO_CHECK, sample_dicts))