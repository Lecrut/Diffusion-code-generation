def find_max_in_2d_array(arr):
    if not arr:
        return None
    max_val = float('-inf')
    for sub_arr in arr:
        if sub_arr:
            max_val = max(max_val, max(sub_arr))
    return max_val
if __name__ == '__main__':
    sample_array = [[3, 5, 1], [8, 2], [], [7]]
    print(find_max_in_2d_array(sample_array))