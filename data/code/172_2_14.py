def validate_keys(keys):
    if not all(isinstance(key, int) and key >= 0 for key in keys):
        raise ValueError("All keys must be non-negative integers.")

def convert_keys_to_labels(keys):
    key_label_mapping = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five'
    }
    return {key: key_label_mapping.get(key, 'Unknown') for key in keys}

if __name__ == '__main__':
    sample_keys = [1, 2, 3, 6]
    validate_keys(sample_keys)
    print(convert_keys_to_labels(sample_keys))