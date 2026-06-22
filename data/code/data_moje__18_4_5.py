def get_middle_value(lst):
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [7],
        [1, 2, 3, 4, 5, 6, 7, 8]
    ]
    for lst in sample_lists:
        result = get_middle_value(lst)
        print(result)