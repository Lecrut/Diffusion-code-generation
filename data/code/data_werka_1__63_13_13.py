def is_non_empty_sequence(sequence):
    return isinstance(sequence, (list, tuple)) and len(sequence) > 0

def get_first_element(sequence):
    if is_non_empty_sequence(sequence):
        return sequence[0]
    return None
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    empty_list = []
    empty_tuple = ()
    non_sequence = 'not a sequence'
    print(get_first_element(sample_list))
    print(get_first_element(sample_tuple))
    print(get_first_element(empty_list))
    print(get_first_element(empty_tuple))
    print(get_first_element(non_sequence))