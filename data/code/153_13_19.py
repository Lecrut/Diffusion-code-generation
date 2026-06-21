def key_exists_in_dicts(key, dict_list):
    return any((key in d for d in dict_list))

if __name__ == '__main__':
    sample_dicts = [{'x': 10}, {'y': 20, 'z': 30}, {'w': 40}]
    key_to_check = 'z'
    result = key_exists_in_dicts(key_to_check, sample_dicts)
    print(result)