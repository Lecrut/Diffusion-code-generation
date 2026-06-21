def middle_value(lst):
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    arrays = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [1, 2],
        [42],
        [5, 6, 7, 8, 9, 10, 11]
    ]
    for arr in arrays:
        print(middle_value(arr))