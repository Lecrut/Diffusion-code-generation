def get_middle_element(sequence):
    if not hasattr(sequence, '__len__') or not hasattr(sequence, '__getitem__'):
        raise TypeError("Input must be a sequence type (list, tuple, str, etc.)")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        mid_index = length // 2
        return sequence[mid_index - 1], sequence[mid_index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        "abcdef",
        (100, 200, 300, 400, 500, 600),
    ]
    for case in test_cases:
        result = get_middle_element(case)
        print(result)
    try:
        get_middle_element([])
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        get_middle_element(12345)
    except TypeError as e:
        print(f"Error caught: {e}")