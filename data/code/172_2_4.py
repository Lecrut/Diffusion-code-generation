def convert_keys_to_labels(keys):
    key_label_mapping = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five'
    }
    if not all(isinstance(key, int) and isinstance(value, str) for key, value in key_label_mapping.items()):
        raise ValueError("All keys must be integers and all values must be strings.")
    
    return {key: key_label_mapping.get(key, 'Unknown') for key in keys}

if __name__ == '__main__':
    sample_keys = [1, 2, 3, 6]
    try:
        print(convert_keys_to_labels(sample_keys))
    except ValueError as e:
        print(e)