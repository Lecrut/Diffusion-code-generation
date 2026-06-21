def extract_keys(source_dict, required_keys):
    if not isinstance(source_dict, dict) or not all(isinstance(k, str) for k in source_dict.keys()):
        raise ValueError("source_dict must be a dictionary with string keys")
    if not isinstance(required_keys, list) or not all(isinstance(k, str) for k in required_keys):
        raise ValueError("required_keys must be a list of strings")

    return {key: source_dict[key] for key in required_keys if key in source_dict}

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    required_keys = ['a', 'c']
    try:
        result = extract_keys(sample_dict, required_keys)
        print(result)
    except ValueError as e:
        print(e)