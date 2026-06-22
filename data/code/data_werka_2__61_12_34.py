def is_valid_sequence(sequence):
    return isinstance(sequence, (list, tuple))

def is_valid_index(sequence, index):
    return 0 <= index < len(sequence)

def get_element(sequence, index):
    if not is_valid_sequence(sequence):
        raise ValueError('Invalid sequence type')
    if not is_valid_index(sequence, index):
        raise ValueError('Index out of range')
    return sequence[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (100, 200, 300, 400, 500)
    print(get_element(sample_list, 2))
    print(get_element(sample_tuple, 3))
    try:
        print(get_element(sample_list, 10))
    except ValueError as e:
        print(e)
    try:
        print(get_element(12345, 1))
    except ValueError as e:
        print(e)