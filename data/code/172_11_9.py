def convert_keys_to_words(keys):
    word_mapping = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        0: 'zero'
    }
    return {key: word_mapping.get(key, 'unknown') for key in keys}

if __name__ == '__main__':
    sample_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(convert_keys_to_words(sample_keys))