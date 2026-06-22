def get_middle_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    middle_index = (length - 1) // 2
    return sequence[middle_index]

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        ["a", "b", "c"],
        ["x", "y"],
        [99],
        [],
        [1, 2, 3, 4, 5, 6, 7, 8]
    ]
    for case in test_cases:
        result = get_middle_item(case)
        print(result)