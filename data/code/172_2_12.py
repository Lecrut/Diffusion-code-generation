def convert_keys_to_labels(keys):
    key_label_mapping = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five'
    }
    result = {}
    for key in keys:
        if not isinstance(key, int) or key < 1 or key > 5:
            raise ValueError(f"Invalid key: {key}. Key must be an integer between 1 and 5.")
        result[key] = key_label_mapping.get(key)
    return result

if __name__ == '__main__':
    sample_keys = [1, 2, 4, 6]
    try:
        labels = convert_keys_to_labels(sample_keys)
        print(labels)
    except ValueError as e:
        print(e)