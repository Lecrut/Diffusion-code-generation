def validate_input(input_list):
    if not all(isinstance(item, int) for item in input_list):
        raise ValueError("Input list must contain only integers")
    if not all(0 <= item <= 9 for item in input_list):
        raise ValueError("Input list contains numbers outside the range [0, 9]")

def numeric_to_word(keys):
    mapping = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    validate_input(keys)
    return {key: mapping.get(key, 'unknown') for key in keys}

if __name__ == '__main__':
    sample_keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numeric_to_word(sample_keys))