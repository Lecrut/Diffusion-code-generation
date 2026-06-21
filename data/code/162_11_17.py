def keys_to_dict(keys):
    if not all(isinstance(key, str) for key in keys):
        raise ValueError("All elements in the input list must be strings.")
    return {key: True for key in keys}

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    result_dict = keys_to_dict(sample_keys)
    print(result_dict)