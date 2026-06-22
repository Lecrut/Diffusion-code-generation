def find_max_in_2d_array(arr):
    if not arr:
        return None
    max_val = float('-inf')
    for sub_arr in arr:
        if sub_arr and sub_arr[0] > max_val:
            max_val = sub_arr[0]
    return max_val
if __name__ == '__main__':
    sample_array = [[3, 5, 1], [2], [], [4, 6]]
    print(find_max_in_2d_array(sample_array))