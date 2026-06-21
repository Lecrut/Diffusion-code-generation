def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    mid_index = length // 2
    return (sequence[mid_index - 1], sequence[mid_index])

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        ['a', 'b', 'c'],
        [5],
        [True, False],
        [7, 8, 9, 10, 11, 12]
    ]
    for case in test_cases:
        result = get_middle_element(case)
        print(result)