def map_keys_to_words(keys):
    if not all(isinstance(k, int) and 0 <= k < 10 for k in keys):
        raise ValueError("All keys must be integers between 0 and 9")
    
    mapping = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    
    return {key: mapping[key] for key in keys}

if __name__ == '__main__':
    sample_keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(map_keys_to_words(sample_keys))