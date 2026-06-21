def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        return sequence[mid_index - 1]
    return sequence[mid_index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        ['a', 'b', 'c'],
        ['x', 'y'],
        [42],
    ]
    for case in test_cases:
        result = get_middle_element(case)
        print(f"Sequence: {case}, Middle: {result}")