def get_middle_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    mid_index_right = length // 2
    mid_index_left = mid_index_right - 1
    if isinstance(sequence, str):
        return sequence[mid_index_right]
    if isinstance(sequence, list) or isinstance(sequence, tuple):
        return sequence[mid_index_right]
    return sequence[mid_index_right]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        "hello",
        "test",
        [],
        [10],
        (7, 8, 9, 10, 11)
    ]
    
    for case in test_cases:
        result = get_middle_item(case)
        print(result)