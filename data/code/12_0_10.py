def get_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    return sequence[(length // 2) - 1]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [42],
        ["a", "b", "c", "d", "e", "f"]
    ]
    for case in test_cases:
        result = get_middle_element(case)
        print(result)