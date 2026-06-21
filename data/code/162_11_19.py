def optimize_string_to_dict(keys):
    return {key: True for key in keys}

if __name__ == '__main__':
    sample_keys = ['apple', 'banana', 'cherry']
    result = optimize_string_to_dict(sample_keys)
    print(result)