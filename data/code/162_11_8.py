def validate_input(data):
    if not isinstance(data, list) or not all(isinstance(key, str) for key in data):
        raise ValueError("Input must be a list of strings")

def keys_to_dict(keys):
    validate_input(keys)
    return {key: True for key in keys}

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    print(keys_to_dict(sample_keys))