def validate_sequence(sequence):
    return hasattr(sequence, '__getitem__') and isinstance(len(sequence), int)

def get_first_element(sequence):
    if not validate_sequence(sequence):
        return None
    try:
        return sequence[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [25, 26, 27]
    sample_tuple = (28, 29, 30)
    empty_list = []
    empty_tuple = ()
    invalid_input = "not a sequence"
    print(get_first_element(sample_list))
    print(get_first_element(sample_tuple))
    print(get_first_element(empty_list))
    print(get_first_element(empty_tuple))
    print(get_first_element(invalid_input))