def get_sublist(large_list, start_index, end_index):
    if not isinstance(large_list, list):
        raise ValueError("The first argument must be a list.")
    if not (isinstance(start_index, int) and isinstance(end_index, int)):
        raise ValueError("Start and end indices must be integers.")
    if start_index < 0 or end_index >= len(large_list):
        raise ValueError("Start index must be non-negative and end index must be within the bounds of the list.")
    if start_index > end_index:
        raise ValueError("Start index cannot be greater than end index.")
    
    return large_list[start_index:end_index + 1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    start = 2
    end = 5
    sub_list = get_sublist(sample_list, start, end)
    print(sub_list)