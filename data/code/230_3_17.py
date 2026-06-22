def extract_and_flatten(data, keys):
    return [item[key] for item in data for key in keys if key in item]

if __name__ == '__main__':
    sample_data = [
        {'a': 1, 'b': 2},
        {'b': 3, 'c': 4},
        {'d': 5}
    ]
    keys_to_extract = ['a', 'b']
    result = extract_and_flatten(sample_data, keys_to_extract)
    print(result)