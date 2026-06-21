def get_middle_value(arr):
    if not arr:
        return None
    mid_index = len(arr) // 2
    return arr[mid_index]

if __name__ == '__main__':
    sample_arrays = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [7],
        [],
        [1, 2],
        [5, 4, 3, 2, 1, 0]
    ]
    for arr in sample_arrays:
        result = get_middle_value(arr)
        print(result)