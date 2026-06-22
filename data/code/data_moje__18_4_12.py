def get_middle_value(lst):
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    arrays = [
        [1, 2, 3],
        [10, 20, 30, 40],
        [5],
        [1, 2, 3, 4, 5, 6, 7],
        [100, 200]
    ]
    for arr in arrays:
        result = get_middle_value(arr)
        print(result)