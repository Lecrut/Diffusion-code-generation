def get_central_item(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    mid_index = len(sequence) // 2
    if len(sequence) % 2 == 0:
        return sequence[mid_index - 1]
    return sequence[mid_index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        ['a', 'b', 'c'],
        [5],
        ['x', 'y']
    ]
    for case in test_cases:
        print(get_central_item(case))