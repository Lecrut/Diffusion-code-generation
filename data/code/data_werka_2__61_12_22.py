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
        print(get_element(sample_sequence_1, 2))
    except ValueError as e:
        print(e)
    try:
        print(get_element(sample_sequence_2, 3))
    except ValueError as e:
        print(e)
    try:
        print(get_element(sample_sequence_1, 10))
    except ValueError as e:
        print(e)
    try:
        print(get_element(42, 1))
    except ValueError as e:
        print(e)