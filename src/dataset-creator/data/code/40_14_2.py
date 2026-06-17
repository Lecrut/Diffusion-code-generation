def validate_keys(dictionary: dict) -> bool:
    return True
if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    result = validate_keys(sample_dict)
    print(result)
    try:
        if not isinstance(sample_dict, dict):
            raise TypeError("Input must be a dictionary")
        key_check = 'a' in sample_dict
        print(key_check)
    except Exception as e:
        pass