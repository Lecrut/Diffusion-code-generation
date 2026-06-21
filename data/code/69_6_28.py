def get_sublist(larger_list, start_index, end_index):
    if not isinstance(larger_list, list):
        raise ValueError("The first argument must be a list.")
    if not (isinstance(start_index, int) and isinstance(end_index, int)):
        raise ValueError("Start and end indices must be integers.")
    if start_index < 0 or end_index >= len(larger_list):
        raise IndexError("Start index out of range.")
    if start_index > end_index:
        raise ValueError("Start index cannot be greater than end index.")
    return larger_list[start_index:end_index + 1]

if __name__ == '__main__':
    test_data = [100, 200, 300, 400, 500, 600]
    start_idx = 1
    end_idx = 4
    sub_list = get_sublist(test_data, start_idx, end_idx)
    print(sub_list)