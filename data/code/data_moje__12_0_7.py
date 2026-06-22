def get_middle_element(sequence):
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    mid_index = len(sequence) // 2
    if len(sequence) % 2 == 1:
        return sequence[mid_index]
    return sequence[mid_index - 1]

if __name__ == '__main__':
    test_cases = [
        [1, 3, 5, 7, 9],
        [2, 4, 6, 8],
        ['a', 'b', 'c'],
        ['x', 'y'],
        [100]
    ]
    for case in test_cases:
        result = get_middle_element(case)
        print(result)