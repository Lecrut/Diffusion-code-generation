def extract_keys(data, key):
    return [item[key] for item in data if key in item]

if __name__ == '__main__':
    sample_data = [
        {'a': 1, 'b': 2},
        {'a': 3, 'c': 4},
        {'d': 5, 'e': 6}
    ]
    result = extract_keys(sample_data, 'a')
    print(result)