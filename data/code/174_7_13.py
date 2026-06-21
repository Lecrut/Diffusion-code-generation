def extract_keys(source_dict, required_keys):
    return {key: source_dict[key] for key in required_keys if key in source_dict}

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    required_keys = ['a', 'c']
    print(extract_keys(sample_dict, required_keys))