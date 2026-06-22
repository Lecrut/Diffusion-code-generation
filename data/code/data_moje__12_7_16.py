def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence is empty")
    middle_index = length // 2
    if length % 2 == 0:
        return sequence[middle_index - 1]
    return sequence[middle_index]

if __name__ == '__main__':
    test_lists = [[1, 2, 3], [1, 2, 3, 4], [5], [], 'abc', 'abcd', (10, 20, 30), (10, 20, 30, 40)]
    for item in test_lists:
        try:
            result = get_middle_element(item)
            print(result)
        except ValueError as e:
            print(e)