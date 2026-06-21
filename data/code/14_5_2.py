THIRD_INDEX = 2
MINIMUM_LENGTH = 3

def get_third_item(sequence):
    sequence_length = len(sequence)
    if sequence_length < MINIMUM_LENGTH:
        raise IndexError("Input sequence must contain at least three items")
    target_value = sequence[THIRD_INDEX]
    return target_value

if __name__ == '__main__':
    sample_numbers = [100, 200, 300, 400]
    third_from_numbers = get_third_item(sample_numbers)
    print(third_from_numbers)
    
    sample_characters = ['x', 'y', 'z']
    third_from_chars = get_third_item(sample_characters)
    print(third_from_chars)
    
    sample_word = "Python"
    third_from_word = get_third_item(sample_word)
    print(third_from_word)
    
    short_sequence = [1, 2]
    try:
        get_third_item(short_sequence)
    except IndexError as error_message:
        print(error_message)