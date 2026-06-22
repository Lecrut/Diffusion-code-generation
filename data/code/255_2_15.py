def find_max_in_2d_array(arr):
    if not arr:
        return None
    max_value = float('-inf')
    for sub_arr in arr:
        for element in sub_arr:
            if element > max_value:
                max_value = element
    return max_value
if __name__ == '__main__':
    sample_array = [[3, 5, 1], [4, 2], [6]]
    print(find_max_in_2d_array(sample_array))