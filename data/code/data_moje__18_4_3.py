def get_middle_value(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30],
        [1, 2, 3, 4],
        [100, 200, 300, 400, 500],
        [42],
        [1, 2]
    ]
    for s in sample_lists:
        print(get_middle_value(s))