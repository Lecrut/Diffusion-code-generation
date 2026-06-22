def extract_and_flatten(data, keys):
    return [item[key] for item in data for key in keys if key in item]

if __name__ == '__main__':
    sample_data = [
        {'a': 1, 'b': 2},
        {'a': 3, 'c': 4},
        {'b': 5, 'd': 6}
    ]
    keys_to_extract = ['a', 'b']
    result = extract_and_flatten(sample_data, keys_to_extract)
    print(result)