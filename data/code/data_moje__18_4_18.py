def get_middle_value(lst):
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    arrays = [
        [1, 2, 3],
        [4, 5, 6, 7],
        [10],
        [1, 2, 3, 4, 5, 6, 7],
        [99, 88, 77]
    ]
    for arr in arrays:
        print(get_middle_value(arr))