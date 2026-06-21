def validate_keys(keys):
    if not all(isinstance(key, (int, float)) for key in keys):
        raise ValueError("All keys must be numeric")
    return keys

def keys_to_words(keys):
    mapping = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    return {key: mapping.get(key, 'unknown') for key in keys}

if __name__ == '__main__':
    sample_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    validated_keys = validate_keys(sample_keys)
    result = keys_to_words(validated_keys)
    print(result)