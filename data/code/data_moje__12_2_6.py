def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    mid = len(sequence) // 2
    if len(sequence) % 2 == 1:
        return sequence[mid]
    return sequence[mid - 1]

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        ["a", "b", "c"],
        [42],
        [1, 2, 3, 4]
    ]
    for case in test_cases:
        print(get_middle_element(case))