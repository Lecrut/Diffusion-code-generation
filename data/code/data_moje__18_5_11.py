def find_middle_index_and_value(array):
    if not array:
        return None, None
    mid_index = len(array) // 2
    mid_value = array[mid_index]
    return mid_index, mid_value

if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [7],
        [],
        [1, 2, 3, 4, 5, 6, 7, 8]
    ]

    for case in test_cases:
        index, value = find_middle_index_and_value(case)
        print(f"Array: {case} -> Index: {index}, Value: {value}")