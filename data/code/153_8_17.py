def validate_key_exists(key, dict_list):
    if not all(isinstance(d, dict) for d in dict_list):
        raise ValueError("dict_list must be a list of dictionaries")
    return any(key in d for d in dict_list)

if __name__ == '__main__':
    sample_dicts = [{'x': 10}, {'y': 20}, {'z': 30}]
    key_to_check = 'y'
    try:
        print(validate_key_exists(key_to_check, sample_dicts))
    except ValueError as e:
        print(e)