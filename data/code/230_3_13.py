def extract_keys(data, keys):
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("All items in the list must be dictionaries.")
    if not all(isinstance(key, str) for key in keys):
        raise ValueError("All keys must be strings.")

    result = []
    for item in data:
        extracted_values = [item[key] for key in keys if key in item]
        result.extend(extracted_values)

    return result

if __name__ == '__main__':
    sample_data = [
        {'a': 1, 'b': 2},
        {'a': 3, 'c': 4},
        {'b': 5, 'd': 6}
    ]
    keys_to_extract = ['a', 'b']
    result = extract_keys(sample_data, keys_to_extract)
    print(result)