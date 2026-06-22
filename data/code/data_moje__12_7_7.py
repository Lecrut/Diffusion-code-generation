def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    middle_index = length // 2
    if length % 2 == 1:
        return sequence[middle_index]
    return (sequence[middle_index - 1], sequence[middle_index])

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        "abcde",
        (100, 200, 300, 400, 500),
        [7],
        "xy",
        list(range(1, 11)),
        tuple(range(1, 12))
    ]
    for case in test_cases:
        result = get_middle_element(case)
        print(f"Input: {case} -> Middle: {result}")