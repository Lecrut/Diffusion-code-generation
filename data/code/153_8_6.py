def validate_key_in_dicts(key, dict_list):
    return all(key in d for d in dict_list)

if __name__ == '__main__':
    sample_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    key_to_check = 'b'
    print(validate_key_in_dicts(key_to_check, sample_dicts))