def validate_keys(required_keys):
    if not isinstance(required_keys, list) or not all(isinstance(key, str) for key in required_keys):
        raise ValueError("required_keys must be a list of strings")

def extract_keys(source_dict, required_keys):
    validate_keys(required_keys)
    return {key: source_dict[key] for key in required_keys if key in source_dict}

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    required_keys = ['a', 'c']
    result = extract_keys(sample_dict, required_keys)
    print(result)