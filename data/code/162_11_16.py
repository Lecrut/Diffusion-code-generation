def validate_keys(keys):
    if not isinstance(keys, list) or not all(isinstance(key, str) for key in keys):
        raise ValueError("Input must be a list of strings")

def keys_to_dict(keys):
    validate_keys(keys)
    return {key: True for key in keys}

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    result_dict = keys_to_dict(sample_keys)
    print(result_dict)