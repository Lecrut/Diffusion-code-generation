def get_middle_item(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    if length % 2 == 1:
        middle_index = length // 2
    else:
        middle_index = (length // 2) - 1
    return sequence[middle_index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [10, 20, 30, 40],
        ['a', 'b', 'c', 'd', 'e'],
        [True, False],
        [42]
    ]
    for case in test_cases:
        result = get_middle_item(case)
        print(result)