def get_middle_value(lst):
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    samples = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [1, 2],
        [42],
        [5, 15, 25, 35, 45, 55, 65]
    ]
    for arr in samples:
        print(get_middle_value(arr))