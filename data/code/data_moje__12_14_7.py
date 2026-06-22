def get_middle_element(sequence):
    if not isinstance(sequence, (list, tuple, str, range)):
        raise TypeError("Input must be a sequence type such as list, tuple, string, or range")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return sequence[length // 2 - 1]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        "python",
        range(1, 6),
        (7, 8, 9, 10, 11, 12),
        [True, False, True],
    ]
    for case in test_cases:
        try:
            result = get_middle_element(case)
            print(f"Input: {case} -> Middle: {result}")
        except (TypeError, ValueError) as e:
            print(f"Input: {case} -> Error: {e}")