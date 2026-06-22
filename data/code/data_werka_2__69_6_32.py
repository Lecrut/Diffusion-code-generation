def get_sublist(large_list, start_index, end_index):
    if not isinstance(large_list, list):
        raise ValueError("The first argument must be a list.")
    if not (isinstance(start_index, int) and isinstance(end_index, int)):
        raise ValueError("Start and end indices must be integers.")
    if start_index < 0 or end_index >= len(large_list) or start_index > end_index:
        raise ValueError("Invalid start or end index.")
    
    return large_list[start_index:end_index + 1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start = 2
    end = 5
    sub_list = get_sublist(sample_list, start, end)
    print(sub_list)