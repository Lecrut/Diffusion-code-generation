def validate_key_exists(key, dict_list):
    return any(key in d for d in dict_list)

if __name__ == '__main__':
    sample_dicts = [{'x': 10}, {'y': 20}, {'z': 30}]
    key_to_check = 'y'
    print(validate_key_exists(key_to_check, sample_dicts))