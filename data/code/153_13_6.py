KEY_TO_CHECK = 'b'
SAMPLE_DICTS = [{'a': 1}, {'b': 2}, {'c': 3}]

def key_exists_in_dicts(key, dict_list):
    return any((key in d for d in dict_list))

if __name__ == '__main__':
    print(key_exists_in_dicts(KEY_TO_CHECK, SAMPLE_DICTS))