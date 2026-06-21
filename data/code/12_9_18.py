def get_middle_item(sequence):
    try:
        length = len(sequence)
        if length == 0:
            return None
        if length % 2 == 1:
            mid_index = length // 2
            return sequence[mid_index]
        else:
            mid_index = length // 2
            return sequence[mid_index - 1], sequence[mid_index]
    except TypeError:
        return None

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [1, 2, 3, 4],
        [42],
        [],
        'abc',
        'abcd',
        (),
        (1, 2, 3),
        (1, 2, 3, 4),
        "hello",
    ]

    for test_input in test_cases:
        result = get_middle_item(test_input)
        print(result)