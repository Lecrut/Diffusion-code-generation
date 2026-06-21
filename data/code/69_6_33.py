def get_sublist(larger_list, start_index, end_index):
    if not isinstance(larger_list, list):
        raise ValueError("The first argument must be a list.")
    if not (isinstance(start_index, int) and isinstance(end_index, int)):
        raise ValueError("Start and end indices must be integers.")
    if start_index < 0 or end_index >= len(larger_list):
        raise IndexError("Index out of range.")
    if start_index > end_index:
        raise ValueError("Start index cannot be greater than end index.")
    return larger_list[start_index:end_index + 1]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_idx = 3
    end_idx = 7
    try:
        result_sublist = get_sublist(sample_data, start_idx, end_idx)
        print(result_sublist)
    except (ValueError, IndexError) as e:
        print(e)