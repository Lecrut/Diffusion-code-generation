def get_middle_value(lst):
    length = len(lst)
    if length == 0:
        return None
    mid_index = length // 2
    return lst[mid_index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        [10, 20, 30, 40],
        [5],
        [1, 2, 3, 4, 5],
        [100, 200]
    ]
    for sample in sample_lists:
        result = get_middle_value(sample)
        print(result)