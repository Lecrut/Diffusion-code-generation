NUM_TO_TEXT_MAP = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five'
}

def convert_keys_to_labels(keys):
    return {key: NUM_TO_TEXT_MAP.get(key, 'Unknown') for key in keys}

if __name__ == '__main__':
    sample_keys = [1, 2, 3, 6]
    print(convert_keys_to_labels(sample_keys))