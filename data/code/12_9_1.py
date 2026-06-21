def get_middle_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 1:
        mid_index = length // 2
    else:
        mid_index = (length // 2) - 1
    return sequence[mid_index]

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [],
        ["a", "b", "c", "d", "e", "f"],
        [42],
        (100, 200, 300),
        []
    ]
    
    for case in test_cases:
        result = get_middle_item(case)
        print(result)