def get_middle_item(sequence):
    length = len(sequence)
    if length == 0:
        return None
    mid_index = length // 2
    if length % 2 == 0:
        return sequence[mid_index - 1]
    return sequence[mid_index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        [10],
        [],
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['x', 'y', 'z']
    ]
    for test_data in test_cases:
        result = get_middle_item(test_data)
        print(result)