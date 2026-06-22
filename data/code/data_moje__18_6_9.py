def get_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [7, 8],
        [42],
        [],
        [1, 2, 3, 4]
    ]
    for sample in sample_lists:
        result = get_middle_element(sample)
        print(result)