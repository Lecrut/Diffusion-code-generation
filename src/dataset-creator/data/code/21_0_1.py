def append_element_to_sequence(sequence: tuple) -> list:
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    try:
        element = next(iter([sequence]))[0]
    except StopIteration:
        return sequence
    result_list = list(sequence) + [element]
    return result_list
if __name__ == '__main__':
    sample_tuple = (1, 2, 3)
    sample_list = ['a', 'b']
    print(append_element_to_sequence(sample_tuple))
    print(append_element_to_sequence(sample_list))