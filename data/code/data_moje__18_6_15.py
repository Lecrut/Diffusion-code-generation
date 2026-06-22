def get_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    test_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        ['a', 'b', 'c'],
        [7],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    for test_list in test_lists:
        result = get_middle_element(test_list)
        print(result)