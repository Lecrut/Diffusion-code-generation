def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    if length % 2 == 0:
        return sequence[length // 2 - 1]
    else:
        return sequence[length // 2]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [1, 2, 3, 4],
        [10, 20, 30, 40, 50],
        [10, 20, 30, 40],
        ('a', 'b', 'c', 'd', 'e'),
        ('x', 'y', 'z', 'w'),
        "hello",
        "worlds",
        [True, False, True],
        [True, False, True, False],
    ]
    for case in test_cases:
        result = get_middle_element(case)
        print(f"Input: {case}, Middle: {result}")
    try:
        get_middle_element([])
    except ValueError as e:
        print(f"Input: [], Error: {e}")