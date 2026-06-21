def map_keys_to_words(keys):
    mapping = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }
    return {key: mapping.get(key, 'unknown') for key in keys}

if __name__ == '__main__':
    sample_keys = [1, 2, 3, 6]
    result = map_keys_to_words(sample_keys)
    print(result)