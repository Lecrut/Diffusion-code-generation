def numeric_to_word(keys):
    mapping = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    return {key: mapping[key] for key in keys if key in mapping}

if __name__ == '__main__':
    sample_keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numeric_to_word(sample_keys))