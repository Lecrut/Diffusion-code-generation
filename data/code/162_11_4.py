def keys_to_dict(keys):
    return {key: True for key in keys}

if __name__ == '__main__':
    sample_keys = ['a', 'b', 'c']
    result = keys_to_dict(sample_keys)
    print(result)