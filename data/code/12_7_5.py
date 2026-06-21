def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    length = len(sequence)
    middle_index = length // 2
    if length % 2 == 0:
        return (sequence[middle_index - 1], sequence[middle_index])
    else:
        return sequence[middle_index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [1, 2, 3, 4],
        [1],
        [1, 2],
        'abcde',
        'abcd',
        (1, 2, 3, 4, 5),
        (1, 2),
        [],
    ]
    for case in test_cases:
        if not case:
            try:
                get_middle_element(case)
            except ValueError as e:
                print(e)
        else:
            print(get_middle_element(case))