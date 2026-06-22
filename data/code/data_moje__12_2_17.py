def get_central_item(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    middle_index = length // 2
    if length % 2 == 1:
        return sequence[middle_index]
    else:
        return sequence[middle_index - 1]

if __name__ == '__main__':
    test_sequence_1 = [1, 2, 3, 4, 5]
    test_sequence_2 = [10, 20, 30, 40]
    test_sequence_3 = ['a', 'b', 'c']
    test_sequence_4 = ['x', 'y']
    print(get_central_item(test_sequence_1))
    print(get_central_item(test_sequence_2))
    print(get_central_item(test_sequence_3))
    print(get_central_item(test_sequence_4))