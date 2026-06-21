def get_element(sequence, index):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError('Invalid sequence type')
    if index < 0 or index >= len(sequence):
        raise ValueError('Index out of range')
    return sequence[index]

if __name__ == '__main__':
    sample_sequence_1 = [5, 15, 25, 35, 45]
    sample_sequence_2 = ('apple', 'banana', 'cherry', 'date', 'elderberry')

    try:
        element_from_list = get_element(sample_sequence_1, 3)
        print(f"Element from list at index 3: {element_from_list}")
    except ValueError as e:
        print(e)

    try:
        element_from_tuple = get_element(sample_sequence_2, 4)
        print(f"Element from tuple at index 4: {element_from_tuple}")
    except ValueError as e:
        print(e)

    try:
        invalid_index_element = get_element(sample_sequence_1, 10)
        print(invalid_index_element)
    except ValueError as e:
        print(e)

    try:
        non_sequence_element = get_element(12345, 1)
        print(non_sequence_element)
    except ValueError as e:
        print(e)