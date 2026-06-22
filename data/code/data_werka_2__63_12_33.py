def get_first_element(sequence):
    if not hasattr(sequence, '__getitem__'):
        return None
    try:
        return sequence[0]
    except (IndexError, TypeError):
        return None

if __name__ == '__main__':
    sample_list = [31, 32, 33]
    sample_tuple = (34, 35, 36)
    empty_list = []
    empty_tuple = ()
    invalid_input = "not a sequence"
    print(get_first_element(sample_list))
    print(get_first_element(sample_tuple))
    print(get_first_element(empty_list))
    print(get_first_element(empty_tuple))
    print(get_first_element(invalid_input))