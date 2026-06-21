EXPECTED_KEY = 'b'

def validate_key_exists(key, dict_list):
    return any((key in d for d in dict_list))
if __name__ == '__main__':
    sample_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    print(validate_key_exists(EXPECTED_KEY, sample_dicts))