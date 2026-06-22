def get_central_item(sequence):
    if not sequence:
        raise ValueError("Cannot get central item from an empty sequence")
    length = len(sequence)
    middle_index = length // 2
    if length % 2 == 1:
        return sequence[middle_index]
    else:
        return sequence[middle_index - 1]

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        ["a", "b", "c", "d", "e", "f"],
        [42],
        [1, 2]
    ]
    for case in test_cases:
        print(get_central_item(case))