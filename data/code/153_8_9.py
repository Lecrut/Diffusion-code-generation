def validate_dict_list(dict_list):
    if not isinstance(dict_list, list) or not all(isinstance(d, dict) for d in dict_list):
        raise ValueError("dict_list must be a list of dictionaries")

def key_exists_in_dicts(key, dict_list):
    validate_dict_list(dict_list)
    return any(key in d for d in dict_list)

if __name__ == '__main__':
    sample_dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
    key_to_check = 'b'
    print(key_exists_in_dicts(key_to_check, sample_dicts))