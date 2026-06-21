def validate_key_exists(key, dict_list):
    return any(key in d for d in dict_list)

if __name__ == '__main__':
    sample_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    key_to_check = 'b'
    print(validate_key_exists(key_to_check, sample_dicts))