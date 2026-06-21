def convert_keys_to_labels(keys):
    mapping = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five'
    }
    return {key: mapping.get(key, f'Unknown_{key}') for key in keys}

if __name__ == '__main__':
    sample_keys = [1, 2, 3, 6]
    print(convert_keys_to_labels(sample_keys))