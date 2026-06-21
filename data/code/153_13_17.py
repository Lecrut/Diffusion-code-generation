def check_key_in_dict_list(key, dict_list):
    return any((key in d for d in dict_list))

if __name__ == '__main__':
    sample_dicts = [{'x': 10}, {'y': 20, 'z': 30}, {'a': 40}]
    key_to_find = 'y'
    
    if check_key_in_dict_list(key_to_find, sample_dicts):
        print(f"The key '{key_to_find}' exists in the list of dictionaries.")
    else:
        print(f"The key '{key_to_find}' does not exist in the list of dictionaries.")