def validate_keys(keys):
    if not all(isinstance(key, int) for key in keys):
        raise ValueError("All keys must be integers.")
    return keys

def convert_key_to_label(key, mapping):
    return mapping.get(key, "Unknown")

def convert_keys_to_labels(keys, mapping):
    validated_keys = validate_keys(keys)
    labels = {key: convert_key_to_label(key, mapping) for key in validated_keys}
    return labels

if __name__ == '__main__':
    sample_mapping = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five'
    }
    sample_keys = [1, 2, 3, 6]
    labels = convert_keys_to_labels(sample_keys, sample_mapping)
    print(labels)