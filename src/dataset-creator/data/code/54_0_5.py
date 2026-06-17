def find_middle_index(arr):
    if len(arr) % 2 != 0:
        return (len(arr)) // 2
    else:
        lower = len(arr) // 2 - 1
        upper = len(arr) // 2
        mid_val_lower = arr[lower]
        mid_val_upper = arr[upper]
        if mid_val_lower <= mid_val_upper:
            return lower
        else:
            return upper
if __name__ == '__main__':
    sample_array = [1, 3, 5, 7, 9, 11]
    index = find_middle_index(sample_array)
    print(index)